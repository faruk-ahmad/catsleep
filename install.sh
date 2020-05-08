cd ..
echo "copying to /home/$(whoami)/ ..."
cp -rf catsleep ~/
cd catsleep
user_config_dir="/home/$(whoami)/.config/autostart"
if [ -d "$user_config_dir" ]; then
    echo "copying catsleep.desktop in $user_config_dir"
    cp -v catsleep.desktop $user_config_dir
    echo "Done ..."
else
    echo "$user_config_dir not exists. installation failed."
fi
echo "Please restart your computer to get work catsleep ..."
