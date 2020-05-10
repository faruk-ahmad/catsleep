cd ..
echo "Uninstalling catsleep..."

src_dir_path="/home/$(whoami)/catsleep"
autostart_file_path="/home/$(whoami)/.config/autostart/catsleep.desktop"
user_config_path="/home/$(whoami)/.catsleep_config.json"


if [[ -f "$user_config_path" ]]
then
    echo "Removing user configuration file..."
    rm -v $user_config_path
fi

if [[ -f "$autostart_file_path" ]]
then
    echo "Removing startup file..."
    rm -v $autostart_file_path
fi

if [[ -d "$src_dir_path" ]]
then
    echo "Removing catsleep source files..."
    rm -rv $src_dir_path
fi

echo "Done."
echo "You need to restart your computer to complete the uninstallation process."
