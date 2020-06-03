mkdir raw_data
cd raw_data
mkdir movies
mkdir tng
mkdir ds9

cd movies
wget http://www.st-minutiae.com/resources/scripts/scripts_mov.zip
unzip scripts_mov.zip

cd ../tng
wget http://www.st-minutiae.com/resources/scripts/scripts_tng.zip
unzip scripts_tng.zip

cd ../ds9
wget http://www.st-minutiae.com/resources/scripts/scripts_ds9.zip
unzip scripts_ds9.zip
