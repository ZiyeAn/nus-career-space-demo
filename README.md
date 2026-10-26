# NUS Career Space — Interactive Demo

基于当前 Figma 方向制作的本地网页原型。无需安装依赖。

## 打开

最方便：双击 `NUS Career Space.html`。它包含完整样式和交互，可以离线打开。

推荐演示：双击 `Start Demo.command`，它会启动本地服务器并打开浏览器。需要电脑已安装 Python 3；在终端按 Control+C 停止。

开发源文件：`index.html`、`styles.css`、`app.js`。修改后重新运行 `python3 build.py` 更新单文件版本。

## 两条流程

1. Plugin demo → Read this page → 检查分类、优先级、材料 → Confirm files & save → Workspace。
2. 直接进入 Today → 自定义任务 / 行业新闻转待办；Interviews → 相关经历与准备笔记 → 选中文字 Ask AI → 继续讨论。Materials & practice 与面试后笔记收在折叠区。

Jobs 含 24 条示例职位、4 个类别，支持侧边筛选、搜索、Columns/Table 切换、右侧详情、任务勾选和进度记录。
Profile 支持简历/作品集的分类和右侧预览。Job Events 收藏后同步到站内日历，也可导出示例日历事件。

## 演示边界

- 所有职位、日期、活动、经历和个人资料均为演示内容，不代表真实招聘或真实学生记录。
- AI 读取、分类与材料匹配是本地规则和预设内容演示，没有连接大模型。粘贴 JD 支持 Role、Company、Location 字段和简单关键词分类；无法分类时手动确认。
- Plugin 是网页内模拟器，不是真正浏览器扩展。
- 新上传文件仅保存在当前浏览器的 IndexedDB，不上传服务器或进行 AI 分析。PDF 和图片支持预览；旧版只记录名称的条目需重新选择原文件。
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

## Interview, advisor, categories and filters update

- Interview questions and suggested answer approaches are combined in one card inside Prepare for this role and in the outline.
- Add interview supports manual company/role/date/time/location/round or linking a saved job. Each interview keeps its own experiences, materials, outline and reflection. October entries appear in the demo calendar.
- AI Chat unsupported questions and explicit human requests link to the official NUS CFG Career Advisory page. No transcript is sent, no appointment is automatically booked.
- Jobs support drag and drop between category columns and an accessible Move to select in cards/table/details. Users can create and rename categories; changes persist locally, including empty columns.
- Job Events topic chips Design and Research combine with OR, Singapore is an AND location filter. All clears these filters.
- Demo question suggestions remain illustrative rather than verified interview reports.

## Resume preview, calendar sync and peach accents

- Profile identity tags removed. Click a material to open a right-side preview. Built-in sample resumes are explicitly labelled demo layouts; they are not personal resume documents.
- New PDF/image uploads are stored in browser-local IndexedDB and previewed using object URLs; no file or chat content is sent to a server. Previous name-only entries ask the user to select the original file. Unsupported formats remain downloadable and are not displayed as a fake preview.
- Saving an event adds it to Today automatically; unsaving removes it. Calendar month controls display October/November and multiple entries per day. View in calendar opens the relevant month; Export .ics remains a separate download.
- #F8AA8E highlights dates, important prompts and states requiring confirmation, while category colours remain distinct.

PDF rendering uses a locally bundled PDF.js 6.4.299 from the official pdfjs-dist npm package (Apache 2.0, see PDFJS-LICENSE). It renders pages directly on the website without sending file data to an external viewer. In-page rendering requires HTTP/HTTPS; the standalone file offers native PDF fallback and a link to use the online demo/local launcher.

## Simplified Today and interview workspace

- Today has a single interview card, editable personal To-do tasks, and two relevant industry stories. Sources and publication dates are visible; the list is a manually verified 26 Oct 2026 snapshot, not an automatic live feed. Following changes topic selection, and Add to tasks converts an application suggestion into an action.
- Jobs can be deleted from cards, table or details with an Undo action. Other interviews and files remain independent.
- Interviews now use a single relevant-experience document rather than a multi-step outline flow. Choose profile experiences, add your own account, and save preparation/review notes per interview. Select document text or notes to reveal Ask AI, or use the per-experience button. The selected text appears visibly in AI Chat and is carried into guided demo replies. No live LLM is connected.
- Avatar opens Log out. This ends only the local demo session; Continue demo restores access without deleting browser-local records or pretending to sign out an actual school account.

News snapshot sources: Figma (23 Oct 2026), https://www.figma.com/blog/how-to-put-your-design-system-to-work-with-the-figma-agent/ ; NUS News (22 Oct 2026), https://news.nus.edu.sg/worlds-first-touchscreen-in-garment ; thoughtbot (20 Oct 2026, updated 22 Oct), https://thoughtbot.com/blog/design-systems-in-an-ai-era ; Figma (15 Oct 2026), https://www.figma.com/blog/design-together-with-code-layers/ . Application suggestions are demo recommendations, not claims from the articles.
