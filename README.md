# pairwise-navmesh-rebake-version

## 领域

游戏、图形与多媒体

## 主题

可破坏场景导航重建

## 说明

请求排队、版本号与增量替换。

初始状态下 `gameplay/navmesh_rebake_version.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
