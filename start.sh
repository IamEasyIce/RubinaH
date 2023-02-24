if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/IamEasyIce/PriyankaH.git /PriyankaH
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /PriyankaH
fi
cd /PriyankaH
pip3 install -U -r requirements.txt
echo "Starting Priyank...."
python3 bot.py
