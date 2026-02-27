
使用python实现，项目管理工具使用pdm,同时版本信息动态使用库中的，项目结构不要使用src布局，而是项目根目录就是项目名称文件夹形式，引入自己库的其他模块或文件时，统一使用 from project.的形式进行引用






### 库使用

如果需要创建结构化数据，优先使用dataclass,如果结构化数据需要从json中加载或者生成json文件，则使用dataclass-json。
如果创建cli工具，则使用google的fire库，并在包装的函数处完善函数的doc

如果创建TUI应用，则使用

日志模块，优先使用loguru，
