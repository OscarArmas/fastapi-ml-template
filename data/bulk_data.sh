#!/bin/bash
echo "Starting data import..."
mongoimport --db test_db --collection item_price_stats --file ./data/items_info.json --jsonArray
echo ls
if [ $? -eq 0 ]; then
    echo "Import completed successfully."
else
    echo "Error during data import."
fi
