# Trek Scraper

A scraper and processor for Star Trek scripts

## Usage

### Download scripts

This grabs scripts in text format for TNG, DS9 and the Star Trek movies and puts them in a folder called `raw_data`

```
sh ./download.sh
```

### Process scripts

This converts the scripts into JSON that we can (hopefully) feed into [script buddy v2](https://github.com/cdpierse/script_buddy_v2)

```
python ./process.py
```

### Using with [Script Buddy](https://github.com/cdpierse/script_buddy_v2)

The above steps create 2 files. Copy both of them to script_buddy_v2/script_buddy/data - this WILL overwrite the existing data files, so you may want to back them up.
