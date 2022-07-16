# SQLite使用总结

<!--ts-->
* [SQLite使用总结](#sqlite使用总结)
   * [简介](#简介)
   * [python: sqlite3库使用](#python-sqlite3库使用)
      * [数据库操作](#数据库操作)
      * [创建连接, 使用上下文自动保持](#创建连接-使用上下文自动保持)
      * [执行sql语句并提交](#执行sql语句并提交)
   * [参考资源](#参考资源)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Tue Jul 12 06:57:18 UTC 2022 -->

<!--te-->

## 简介

```admonish quote title='wikipedia: SQLite就是一个嵌入式数据库'
SQLite（/ˌɛskjuːɛlˈlaɪt/[5]或/ˈsiːkwəl.laɪt/[6]）是遵守ACID的关系数据库管理系统，它包含在一个相对小的C程序库中。
1. "嵌入式"数据库：与许多其它数据库管理系统不同，SQLite不是一个客户端/服务器结构的数据库引擎，而是被集成在用户程序中。
2. SQLite遵守ACID，实现了大多数SQL标准。
3. 它使用动态的、弱类型的SQL语法。
4. 它作为嵌入式数据库，是应用程序，如网页浏览器，在本地/客户端存储数据的常见选择。
5. 它可能是最广泛部署的数据库引擎，因为它正在被一些流行的浏览器、操作系统、嵌入式系统所使用[
6. 同时，它有许多程序设计语言的语言绑定, 比如python内置SQLite的支持
```

> SQLite 是一个C语言库，它可以提供一种轻量级的基于磁盘的数据库，这种数据库不需要独立的服务器进程，也允许需要使用一种非标准的 SQL 查询语言来访问它。一些应用程序可以使用 SQLite 作为内部数据存储。可以用它来创建一个应用程序原型，然后再迁移到更大的数据库，比如 PostgreSQL 或 Oracle。

## python: sqlite3库使用

### 数据库操作

SQLite的存在形式就是一个文本文件，所以一般一个文件就是一个数据库。

```python
{{#include ../../codes/sqlite_python.py:1:4}}
```

### 创建连接, 使用上下文自动保持

```python
{{#include ../../codes/sqlite_python.py:6:9}}
```

### 执行sql语句并提交

## 参考资源

- [SQLite - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/SQLite)
- [sqlite3 --- SQLite 数据库 DB-API 2.0 接口模块 — Python 3.10.5 文档](https://docs.python.org/zh-cn/3/library/sqlite3.html)