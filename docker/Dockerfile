# 使用 Ubuntu 22.04 作為基礎映像
FROM ubuntu:22.04

# 設置環境變量以避免交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 更新包列表並安裝 OpenSSH 服務
RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get clean
RUN apt-get -y update
RUN apt-get install -y git sudo curl unzip gcc ripgrep ca-certificates apt-transport-https build-essential
RUN git config --global http.sslbackend schannel

# Install zoxide
RUN apt install -y zoxide
RUN echo 'eval "$(zoxide init bash)"' >> ~/.bashrc

# Install python3-pip
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip

# Install Uv
RUN pip install uv

# Install Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc
ENV PATH="/root/.cargo/bin:${PATH}"

# Install Zellij
RUN /root/.cargo/bin/cargo install --locked zellij

# Install nvim
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:neovim-ppa/unstable
RUN apt-get install -y neovim

# Instal node.js
RUN curl -o- https://fnm.vercel.app/install | bash
RUN /root/.local/share/fnm/fnm install 22

# Install OuYang's nvim config
RUN git config --global http.sslbackend gnutls
RUN mkdir ~/.config
RUN cd ~/.config
RUN git clone https://github.com/OuYangMinOa/neovim_setup ~/.config/nvim

# Install fzf
RUN git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
RUN ~/.fzf/install --key-bindings --completion --update-rc

# Install oh-myposh
RUN curl -s https://ohmyposh.dev/install.sh | bash -s

# Add command to .bashrc
RUN echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
RUN echo 'eval "$(oh-my-posh init bash --config ~/.cache/oh-my-posh/themes/amro.omp.json)"' >> ~/.bashrc
RUN mkdir /root/project
RUN update-ca-certificates

# 創建 SSH 服務的必要目錄
RUN mkdir /var/run/sshd
# 設置 root 密碼（請根據需要更改密碼）
RUN echo 'root:root' | chpasswd
# 允許 root 用戶通過 SSH 登錄
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# 開放 SSH 端口
EXPOSE 22

# 啟動 SSH 服務
CMD ["/usr/sbin/sshd", "-D"]