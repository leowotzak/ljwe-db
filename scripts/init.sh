
apt update && apt upgrade -y
apt install postgresql postgresql-contrib -y
sudo -u postgres createuser database
sudo -u postgres createdb SecuritiesMaster
psql -u postgres -c "alter user database with encrypted password 'password';"
psql -u postgres -c "grant all privileges on database 'SecuritiesMaster' to database;"
