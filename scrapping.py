import os
import csv
import logging
from google_play_scraper import reviews, Sort

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_reviews(app_id, lang, country, sort, count):
    all_reviews = []
    token = None
    fetched_count = 0

    while fetched_count < count:
        try:
            batch_count = min(1000, count - fetched_count)
            logging.info(f"Fetching batch: {fetched_count} / {count} ulasan")

            current_reviews, token = reviews(
                app_id=app_id,
                lang=lang,
                country=country,
                sort=sort,
                count=batch_count,
                continuation_token=token  # pagination
            )
            if not current_reviews:
                logging.info("Tidak ada ulasan  yang ditemukan.")
                break

            all_reviews.extend(current_reviews)
            fetched_count += len(current_reviews)

            if token is None:
                break
        except Exception as e:
            logging.error(f"Terjadi error saat mengambil ulasan: {e}")
            break

    return all_reviews


def save_reviews_to_csv(reviews_list, directory, filename):
    if not reviews_list:
        logging.info("Tidak ada ulasan untuk disimpan.")
        return

    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)

    # Get all possible keys dynamically
    all_keys = set()
    for review in reviews_list:
        all_keys.update(review.keys())

    all_keys = list(all_keys)  # Convert to list for CSV header

    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=all_keys)
            writer.writeheader()
            for review in reviews_list:
                writer.writerow({key: review.get(key, '') for key in all_keys})

        logging.info(f"Ulasan berhasil disimpan ke {file_path}")
    except Exception as e:
        logging.error(f"Terjadi error saat menulis ke file CSV: {e}")


def main():
    app_id = 'com.tencent.ig'
    lang = 'id'
    country = 'id'
    sort = Sort.MOST_RELEVANT
    count = 15000

    reviews_list = fetch_reviews(app_id, lang, country, sort, count)
    if reviews_list:
        save_reviews_to_csv(reviews_list, 'data', 'ulasan.csv')
    else:
        logging.info("Tidak ada ulasan yang berhasil diambil.")


if __name__ == "__main__":
    main()
