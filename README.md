# Instagram Followers Checker

A simple Python utility to analyze your Instagram followers and following lists.

## Description

This script helps you analyze data exported from Instagram (in JSON format) to find:
- **Mutual followers**: users you follow who also follow you back.
- **Unfollowers**: users you follow who do not follow you back.

## How it works

1. **Export** your Instagram data from your account (see the "Your Instagram Data" section) and place the `following.json` and `followers_1.json` files inside the `metadata/` folder of this repository.
2. **Run** the main script:

    ```bash
    python main.py
    ```

3. The script will print to the terminal your mutual followers and unfollowers.

## Project structure
```crmsh
instagram-followers-checker/
│
├── metadata/
│   ├── following.json
│   └── followers_1.json
│
├── service/
│   └── Checker.py
│
├── .gitignore
├── LICENSE
├── main.py
└── requirements.txt
```

## Dependencies

- Python 3.x

All required Python dependencies are listed in `requirements.txt`.

To install them, run:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the GPL-3.0 license.
