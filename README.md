# 长门实验中学试题自动批改系统
基于书生浦语大模型
这是一个为教师设计的智能试题作业批改工具，旨在简化标准化题目的批改流程并提升效率。

---

## 📌 功能亮点

- **自动化批改**：支持对选择题、填空题等标准化题目类型进行自动评分。
- **OCR 文件解析**：通过 MinerU 实现 PDF、图片等多种格式文件的内容提取与解析。
- **AI 辅助评分**：结合大模型（如 DeepSeek）实现智能化主观题评分建议。
- **多格式支持**：兼容 PDF、Word、图片等多种学生作业上传格式。
- **成绩统计分析**：自动汇总学生成绩，并提供错题分布与教学反馈。
- **用户权限管理**：区分教师与学生角色，保障数据安全与隐私。

---

## ⚙️ 技术栈

| 类别 | 技术/框架 |
|------|-----------|
| 后端 | Python (FastAPI) |
| 前端 | React / Vue.js（待开发） |
| 数据库 | PostgreSQL / MySQL（待集成） |
| 文件处理 | MinerU OCR 解析服务 |
| AI 模型 | OpenRouter + 书生浦语大模型 |
| 部署 | Docker + Kubernetes 或云平台部署 |

---

## 📁 项目结构
- project-root/
  - app/
    - main.py
    - config.py
    - utils.py
    - models/
      - schemas.py
    - routers/
      - files.py
      - submissions.py
    - services/
      - mineru_service.py
      - grading_service.py
  - core/
    - ai/
      - grading_model.py
  - uploads/
  - .env
  - requirements.txt
  - README.md

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yourname/grading-system.git
cd grading-system
```
2. 安装依赖
```bash
pip install -r requirements.txt
```
3. 配置环境变量
创建 .env 文件并添加如下内容：
```bash
env
MINERU_AUTH_TOKEN=Bearer your_mineru_token_here
OPENROUTER_API_KEY=your_openrouter_key_here
```
4. 启动服务
```bash
uvicorn app.main:app --reload
访问：http://localhost:8000/docs 可查看并测试 API 文档。
```

##🧪 主要接口说明

| 接口    | 方法 | 描述 |
|----------|:----:|-----:|
| files/ | upload	POST  |上传文件并触发 MinerU 解析任务  |
| files/results/ | {batch_id}	GET	  | 查询文件解析状态及结果地址 |
| submissions/   | grade	POST | 提交学生答案与标准答案进行自动评分  |


##📝 使用说明

教师操作流程：
- 上传试卷 PDF/Word/图片等格式的作业文件。
- 系统自动调用 MinerU 解析试卷内容。
- 教师输入参考答案与学生作答内容。
- 系统返回 AI 自动生成的评分与评语。
- 支持导出成绩报告（Excel/PDF 格式）。


##🛠️ 开发建议

- 使用 pytest 编写单元测试，确保核心模块稳定性。
- 添加日志记录 (logging) 替代 print()，方便调试。
- 集成数据库支持（PostgreSQL/MySQL），用于保存历史批改记录。
- 后续可引入前端页面，提供完整的 UI 操作体验。


##📦 未来扩展方向

- 引入 WebSocket 实现实时评分进度推送
- 支持多题批量评分接口
- 图像预览与标注工具
- 成绩报表导出为 Excel 或 PDF
- 用户身份验证与权限管理模块


##🤝 贡献指南

- 欢迎贡献代码、改进功能或提交 issue。请遵循以下步骤：
- Fork 本仓库
- 创建新分支（feature/xxx）
- 提交 Pull Request 并描述改动
- 保持代码规范和注释完整


##💬 联系我们

- 如果你有任何建议、问题或合作意向，请联系作者邮箱或提交 issue。


##本项目受 MIT 许可证保护


##本README由书生浦语大模型生成

