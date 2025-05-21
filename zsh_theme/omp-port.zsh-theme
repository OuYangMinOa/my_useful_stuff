# omp-port.zsh-theme  ───  Nerd Font / True-color 終端最佳
# ----------------------------------------------------------
# 第 1 行：Python venv -─> 使用 U+E235 ；使用者圖示（U+EB99）＋名稱；資料夾圖示（U+F07B）＋目前路徑；Git 狀態
# 第 2 行：若當前是 root（UID 0）顯示圖示 U+E3BF，再接玫瑰紅色「# 」

# ---------- ANSI/truecolor（%F{#rrggbb}）調色盤 ----------
local CLR_VENV='%F{#afff2f}'
local CLR_USER='%F{#45F1C2}'
local CLR_PATH='%F{#0CA0D8}'
local CLR_GIT='%F{#14A5AE}'
local CLR_ROOT='%F{#cd5e42}'
local CLR_HASH='%F{#CD4277}'
local CLR_RESET='%f%k'

# ---------- 1. Python 虛擬環境 ----------
function _omp_python_venv() {
  [[ -n "$VIRTUAL_ENV" ]] || return
  print -n "${CLR_VENV}\uE235 ${${VIRTUAL_ENV:t}}${CLR_RESET} "
}

# ---------- 2. 使用者 / 工作階段 ----------
function _omp_session() {
  print -n "${CLR_USER}\uEB99 %n on${CLR_RESET} "
}

# ---------- 3. 目前路徑 ----------
function _omp_path() {
  print -n "${CLR_PATH}\uF07B %~ ${CLR_RESET}"
}

# ---------- 4. Git 狀態（分支＋stash 計數） ----------
function _omp_git() {
  git rev-parse --is-inside-work-tree &>/dev/null || return
  local branch stash upstream=''
  branch=$(git symbolic-ref --quiet --short HEAD 2>/dev/null \
        || git describe --tags --exact-match 2>/dev/null)
  stash=$(git stash list 2>/dev/null | wc -l | tr -d ' ')
  git rev-parse @{u} &>/dev/null && upstream='⇵'

  print -n "${CLR_GIT}${upstream}${branch}"
  (( stash > 0 )) && print -n " \uEB4B ${stash}"
  print -n "${CLR_RESET} "
}

# ---------- 5. 第二行：root 圖示 + 提示字元 ----------
function _omp_second_line() {
  local icon='' ; (( EUID == 0 )) && icon="${CLR_ROOT}\uE3BF ${CLR_RESET}"
  print -n "\n${icon}${CLR_HASH}# ${CLR_RESET}"
}

# ---------- 組合 PROMPT ----------
precmd() {
  PROMPT="$(_omp_python_venv)$(_omp_session)$(_omp_path)$(_omp_git)$(_omp_second_line)"
  RPROMPT=''        # 右側留空；需要可自行加東西
}

# 呼叫一次以立即生效
precmd
