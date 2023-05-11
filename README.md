# 贴吧签到Github Action版

## 使用说明

1. Fork 本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets and variables 这一项，在Actions添加一个环境变量。其中 `COOKIE` 存放你的 cookie。支持同时添加多个帐户，cookie隔行放置即可。

[![p9rJxGq.jpg](https://s1.ax1x.com/2023/05/11/p9rJxGq.jpg)](https://imgse.com/i/p9rJxGq)

2. 设置好环境变量后点击你的仓库上方的 `Actions` 选项，第一次打开需要点击 `I understand...` 按钮，确认在 Fork 的仓库上启用 GitHub Actions 。

3. 任意发起一次commit，触发action。

4. 至此自动签到就搭建完毕了，可以再次点击`Actions`查看工作记录，如果有`Baidu Tieba Auto Sign`则说明workflow创建成功了。点击右侧记录可以查看详细签到情况。
