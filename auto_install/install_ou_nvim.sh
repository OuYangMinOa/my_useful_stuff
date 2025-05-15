apt-get update -y
apt-get install -y git sudo curl unzip gcc ripgrep ca-certificates
apt install -y software-properties-common
add-apt-repository -y ppa:neovim-ppa/unstable
apt-get install -y neovim
git config --global http.sslbackend gnutls schannel
curl -o- https://fnm.vercel.app/install | bash
/root/.local/share/fnm/fnm install 22
mkdir ~/.config
cd ~/.config
git clone https://github.com/OuYangMinOa/neovim_setup ~/.config/nvim
rm ~/.config/nvim/lua/plugins/fold.lua
rm ~/.config/nvim/readme.md
rm -rf  ~/.config/nvim/.git
rm -rf  ~/.config/nvim/images
source ~/.bashrc
nvim --headless +qall
# git config --global http.sslbackend gnutls schannel

