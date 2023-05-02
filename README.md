# csv-load-age
### Project Setup 

- **Clone the repository**

```
git clone https://github.com/Zainab-Saad/csv-load-age.git
```

- **Checkout out to the cloned directory**
```
cd csv-load-age/python
```

- **Install prerequisites**
```
sudo apt-get update
sudo apt-get install python3-dev libpq-dev
```

- **Install Dependencies**
```
pip install -r requirements.txt
```

- **Build From source**
```
sudo python3 setup.py install
```

> You should now have a postgres instance running on your system

- **Set DSN**
Set DSN in 'test_load_csv_to_age.py' and 'test_load_age_to_csv.py'

### Load CSV to AGE, AGE to CSV
- Run the files 'test_load_csv_to_age.py' and 'test_load_age_to_csv.py' as it is or change the file paths in function arguments as per the requirement.