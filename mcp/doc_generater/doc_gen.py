

from dataclasses import dataclass
from string import Template
from fastmcp import Context, FastMCP


from typing import Literal

# 获取当前脚本所在目录
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
TEMPLATE_FILE = SCRIPT_DIR / "template.md"

OUTPUT_DOCS = SCRIPT_DIR.parent / "out.md"
OUTLINE_DOCS = SCRIPT_DIR.parent / "sheet.csv"


from loguru import logger


logger.remove()

logger.add("logs/mcp.log")



@dataclass
class InterfaceDoc:
    title: str
    description: str
    ros_type: str
    data_type: str
    add_version: str
    cli_code: str
    example_code: str



    def generate_context(self) -> str:

        if not TEMPLATE_FILE.exists():

            return ""

        template_content = TEMPLATE_FILE.read_text()

        
        # 准备参数字典
        py_var = {
            "py_title": self.title,
            "py_desc": self.description,
            "py_ros_type": self.ros_type,
            "py_data_type": self.data_type,
            "py_add_version": self.add_version,
            "py_cli": self.cli_code,
            "py_example": self.example_code,
        }
        

        # for key, value in py_var.items():
        #     print(f"  {key}: {value[:50]}..." if len(str(value)) > 50 else f"  {key}: {value}")

        # 使用Template进行变量替换
        template = Template(template_content)

        context = template.safe_substitute(py_var)


        return context



app = FastMCP("doc_generator", "1.0.0")



@app.tool()
def generate_document(
    title: str,
    description: str,
    ros_type: Literal["Service", "Topic/Subscribe", "Topic/Publish", "Action"],
    data_type: str,
    add_version: str,
    cli: str = "",
    example: str = "",
) -> bool:
    """生成接口文档 Markdown 文本。

    这个 MCP 工具基于模板渲染接口文档，直接将符合规则的内容写入到文件中

    Args:
        title: 接口名称，对应模板中的 `{py_title}`。
        description: 接口描述，支持多行文本。
        ros_type: ROS 接口类型，可选值为 "Service" | "Topic/Subscribe" | "Topic/Publish" | "Action"。
        data_type: 话题/服务的数据类型标识。
        add_version: 首次添加该接口的版本号。
        cli: 可选的 CLI 示例，会渲染到模板 `{py_cli}` 占位符。
        example: 可选的代码示例，填充 `{py_example}` 占位符。

    Returns:
        bool: 返回True代表调用成功
    """
    # 调试信息开始
    logger.info("=" * 50)

    # 创建文档对象
    doc = InterfaceDoc(title, description, ros_type, data_type, add_version, cli, example)
    logger.info(f"[调试] 创建的 InterfaceDoc 对象: {doc}")
    
    # 生成文档内容
    context = doc.generate_context()


    logger.info("=" * 50)
    # 调试信息结束
    
    # OUTPUT_DOCS.write_text(context)
    with open(OUTPUT_DOCS, "a", encoding="utf-8") as f:
        f.write(f"{context}\n\n")


    return True



@app.tool()
def generate_ros_interface_outline( title: str,
    description: str,
    ros_type: Literal["Service", "Topic/Subscribe", "Topic/Publish", "Action"],
    data_type: str,
    add_version: str):
    """生成接口文档 大纲。

    这个 MCP 工具生成符合接口文档大纲的内容，直接将符合规则的内容写入到文件中

    Args:
        title: 接口名称，对应模板中的 `{py_title}`。
        description: 接口描述，支持多行文本。
        ros_type: ROS 接口类型，可选值为 "Service" | "Topic/Subscribe" | "Topic/Publish" | "Action"。
        data_type: 话题/服务的数据类型标识。
        add_version: 首次添加该接口的版本号。

    Returns:
        bool: 返回True代表调用成功
    """

    with open("sheet.csv", "a", encoding="utf-8") as f:
        f.write(f"{title},{description}, {ros_type}, {data_type}, ,{add_version}, , ,\n")
    return True



if __name__ == "__main__":

    app.run(transport="stdio")
    # doc = InterfaceDoc("title", "description", "ros_type", "data_type", "add_version", "cli_code", "example_code")

    # with open(OUTPUT_DOCS, "a", encoding="utf-8") as f:
    #     f.write(f"{doc.generate_context()}\n\n")
