if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/IamEasyIce/RubinaH.git /RubinaH
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RubinaH
fi
cd /RubinaH
pip3 install -U -r requirements.txt
echo "Starting Rubina...."
python3 bot.py
