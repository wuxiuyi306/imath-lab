# 智能数学学习系统 (iMathLab)

## 项目简介

一个基于最先进技术栈打造的初中数学智能学习平台，致力于通过深入浅出的方式讲解数学原理，培养数学思维。本系统特别注重知识点的底层逻辑解析和思维拓展，让学习数学变得新颖、有趣且富有洞察力。

## 技术栈

### 前端
- Next.js - React框架
- TailwindCSS - 样式框架
- TypeScript - 类型安全
- Class Variance Authority - 组件变体管理

### 后端
- FastAPI - Python异步Web框架
- MongoDB - 数据库
- Redis - 缓存
- JWT - 认证
- 微信小程序登录集成

## 系统特点

### 1. 完整的知识体系
- 全面覆盖初中数学知识点
- 基于专业数学教育视角的知识点分析
- 灵活的知识体系扩展性
- 跨章节知识关联和整合

### 2. 深度教学系统
- 知识点底层逻辑解析
  * 数学概念本质探讨
  * 公式推导逻辑链条
  * 定理背后的思维方式
- 思维拓展训练
  * 多维度思考方法
  * 创新解题思路
  * 数学思维培养
- 知识关联体系
  * 概念间的逻辑联系
  * 知识应用场景分析
  * 中考真题对应分析

### 3. 智能学习功能
- 交互式学习体验
- 个性化学习路径
- 智能题型推荐系统
  * 基于错题分析的相似题型推荐
  * 针对性练习和巩固
  * 难度递进的练习序列
  * 实时反馈和解析
- AI辅助学习（基于阿里通义千问）
  * 智能解答
  * 个性化讲解
  * 随时提问的智能助手

### 4. 用户系统（简约设计）
- 微信扫码登录
  * 无需账号密码
  * 仅需微信用户名
- 学习数据管理
  * 学习进度追踪
  * 错题集管理
  * 个性化推荐

## 项目结构

```
iMathLab/
├── frontend/              # 前端项目
│   ├── src/
│   │   ├── app/          # 页面
│   │   ├── components/   # 组件
│   │   ├── lib/          # 工具函数
│   │   └── styles/       # 样式
│   ├── package.json
│   └── ...
│
├── backend/              # 后端项目
│   ├── app/
│   │   ├── auth/        # 认证
│   │   ├── models/      # 数据模型
│   │   ├── routers/     # API路由
│   │   └── services/    # 业务逻辑
│   ├── main.py
│   └── ...
│
└── DEVELOPMENT_PLAN.md   # 开发计划
```

## 快速开始

### 前端开发

```bash
cd frontend
npm install
npm run dev
```

### 后端开发

```bash
cd backend
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
pip install -r requirements.txt
python run.py
```

## 环境变量

1. 前端环境变量 (frontend/.env.local)：
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

2. 后端环境变量 (backend/.env)：
```env
# 复制.env.example并填写相应的值
cp .env.example .env
```

## 功能特点

1. 知识点系统
   - 系统化的数学知识点讲解
   - AI助手辅助学习
   - 知识点关联图谱

2. 练习系统
   - 智能题目推荐
   - AI批改和解析
   - 拍照解题

3. 错题本系统
   - 智能错题归类
   - 知识点关联分析
   - 针对性练习推荐

## 开发规范

1. Git提交规范
   - feat: 新功能
   - fix: 修复bug
   - docs: 文档更新
   - style: 代码格式（不影响代码运行的变动）
   - refactor: 重构
   - test: 增加测试
   - chore: 构建过程或辅助工具的变动

2. 代码规范
   - 使用ESLint和Prettier
   - 遵循PEP 8 Python代码规范
   - 编写单元测试

## 贡献指南

1. Fork本仓库
2. 创建你的特性分支 (git checkout -b feature/AmazingFeature)
3. 提交你的改动 (git commit -m 'Add some AmazingFeature')
4. 推送到分支 (git push origin feature/AmazingFeature)
5. 开启一个Pull Request

## 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详细信息
