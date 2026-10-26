# NUS Career Space — Interactive Demo

基于当前 Figma 方向制作的本地网页原型。无需安装依赖。

## 打开

最方便：双击 `NUS Career Space.html`。它包含完整样式和交互，可以离线打开。

推荐演示：双击 `Start Demo.command`，它会启动本地服务器并打开浏览器。需要电脑已安装 Python 3；在终端按 Control+C 停止。

开发源文件：`index.html`、`styles.css`、`app.js`。修改后重新运行 `python3 build.py` 更新单文件版本。

## 两条流程

1. Plugin demo → Read this page → 检查分类、优先级、材料 → Confirm files & save → Workspace。
2. 直接进入 Today → Generate outline；或 Interviews → Prepare materials → 选经历 → 确认材料 → 生成提纲 → VMock 外链 → 面试后复盘。

Jobs 含 24 条示例职位、4 个类别，支持侧边筛选、搜索、Columns/Table 切换、右侧详情、任务勾选和进度记录。
Profile 支持添加简历/作品集的文件名和分类。Job Events 支持保存与导出示例日历事件。

## 演示边界

- 所有职位、日期、活动、经历和个人资料均为演示内容，不代表真实招聘或真实学生记录。
- AI 读取、分类与材料匹配是本地规则和预设内容演示，没有连接大模型。粘贴 JD 支持 Role、Company、Location 字段和简单关键词分类；无法分类时手动确认。
- Plugin 是网页内模拟器，不是真正浏览器扩展。
- 上传仅保存文件名与分类，不上传、持久保存或分析文件内容。
- 任务、职位、材料名、笔记和复盘使用浏览器 localStorage 保存；不同浏览器和打开方式的数据可能不同。Reset demo 可恢复初始数据。
- 公司链接是招聘首页或公司网站，不是经过验证的具体岗位投递链接。VMock 是外部入口，可能需要学校账户。
- 没有后端、登录、真实投递、录音评分或外部消息发送。活动导出清楚标记 Demo。

## 本次验证

浏览器走通 Plugin 读取、匹配材料、保存与 Workspace 连接；验证 Jobs 表格切换、类别筛选、右侧详情和 Applied 更新；验证选经历、确认材料、生成面试提纲。JavaScript 语法检查通过。

## UI update

- Today：点击日历日期显示事件小窗，可进入对应投递或面试准备。支持外部点击和 Escape 关闭。
- Interviews：在 Prepare for this role 上方新增 AI interview research，预览三类可能问题，并将问题带入经历选择与提纲。当前仅为明确标记的模拟检索，不声称已抓取真实面经。
- Plugin：固定 384px 宽度，窄屏横向滚动，不压缩为网页自适应面板。

## Global AI Chat & interview layout

Top nav includes an AI Chat side panel available from every page. This is a browser-local guided-reply demo (English and Chinese keywords), not a live LLM. It supports free-text input, suggested questions, current demo data, navigation actions, Enter to send, Shift+Enter for a newline, Escape to close, and clearing the conversation. Messages are kept only for the current page session and are not sent to a server. Interview inner pages now use the full workspace width with a compact context column, a prominent 52px Back to Interviews button and a separate previous-step control.
