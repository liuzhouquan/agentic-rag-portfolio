# test_structured_output.py
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List

# 使用项目中的 schema
class QueryAnalysis(BaseModel):
    is_clear: bool = Field(
        description="Indicates if the user's question is clear and answerable."
    )
    questions: List[str] = Field(
        description="List of rewritten, self-contained questions."
    )
    clarification_needed: str = Field(
        description="Explanation if the question is unclear."
    )

def get_llm():
    """获取 LLM 实例"""
    api_key = config.DASHSCOPE_API_KEY
    if not api_key:
        raise ValueError("请设置 DASHSCOPE_API_KEY（环境变量或 config_secrets.json）")
    
    return ChatOpenAI(
        model=config.LLM_MODEL,
        api_key=api_key,
        base_url=config.DASHSCOPE_BASE_URL,
        temperature=config.LLM_TEMPERATURE
    )

def test_bind_tools():
    """测试 bind_tools 是否支持"""
    print("=" * 50)
    print("测试 1: bind_tools 支持")
    print("=" * 50)
    
    llm = get_llm()
    
    try:
        # ... 其余代码保持不变
        from langchain_core.utils.function_calling import convert_to_openai_tool
        tool_schema = convert_to_openai_tool(QueryAnalysis)
        print(f"✅ Tool schema 转换成功:")
        print(f"   Name: {tool_schema['function']['name']}")
        
        llm_with_tool = llm.bind_tools([QueryAnalysis], tool_choice="any")
        print(f"✅ bind_tools 成功")
        
        response = llm_with_tool.invoke("分析这个问题：什么是AI？")
        print(f"✅ LLM 调用成功")
        print(f"   Response type: {type(response)}")
        print(f"   Has tool_calls: {hasattr(response, 'tool_calls') and response.tool_calls}")
        
        if hasattr(response, 'tool_calls') and response.tool_calls:
            print(f"   Tool calls: {response.tool_calls}")
            from langchain_core.output_parsers import PydanticToolsParser
            parser = PydanticToolsParser(tools=[QueryAnalysis], first_tool_only=True)
            parsed = parser.invoke(response)
            print(f"✅ 解析成功: {parsed}")
        else:
            print(f"⚠️  LLM 没有返回 tool_calls")
            print(f"   Content: {response.content}")
            
    except Exception as e:
        print(f"❌ bind_tools 失败: {e}")
        import traceback
        traceback.print_exc()

def test_with_structured_output():
    """测试 with_structured_output 是否支持"""
    print("\n" + "=" * 50)
    print("测试 2: with_structured_output 支持")
    print("=" * 50)
    
    llm = get_llm()
    
    try:
        llm_structured = llm.with_structured_output(QueryAnalysis, method="function_calling")
        print(f"✅ with_structured_output 创建成功")
        
        result = llm_structured.invoke("分析这个问题：什么是AI？")
        print(f"✅ 调用成功")
        print(f"   Result type: {type(result)}")
        print(f"   Result: {result}")
        print(f"   is_clear: {result.is_clear}")
        print(f"   questions: {result.questions}")
        
        return True
    except NotImplementedError as e:
        print(f"❌ with_structured_output 不支持: {e}")
        return False
    except Exception as e:
        print(f"❌ with_structured_output 调用失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_manual_implementation():
    """手动实现结构化输出（如果 with_structured_output 不支持）"""
    print("\n" + "=" * 50)
    print("测试 3: 手动实现结构化输出")
    print("=" * 50)
    
    llm = get_llm()
    
    try:
        llm_with_tool = llm.bind_tools([QueryAnalysis], tool_choice="any")
        response = llm_with_tool.invoke("分析这个问题：什么是AI？")
        print(f"✅ LLM 响应: {response}")
        
        if hasattr(response, 'tool_calls') and response.tool_calls:
            from langchain_core.output_parsers import PydanticToolsParser
            parser = PydanticToolsParser(tools=[QueryAnalysis], first_tool_only=True)
            parsed = parser.invoke(response)
            print(f"✅ 手动解析成功: {parsed}")
            return parsed
        else:
            print(f"⚠️  没有 tool_calls，尝试从 content 解析")
            import json
            import re
            content = response.content
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                parsed = QueryAnalysis(**data)
                print(f"✅ 从 content 解析成功: {parsed}")
                return parsed
            else:
                print(f"❌ 无法解析 content: {content}")
                return None
                
    except Exception as e:
        print(f"❌ 手动实现失败: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    # 设置 API Key（从 config 模块读取，支持环境变量和 secrets.json）
    if not config.DASHSCOPE_API_KEY:
        print("⚠️  请设置 DASHSCOPE_API_KEY")
        print("   方式1: 设置环境变量")
        print("         export DASHSCOPE_API_KEY='your-api-key'")
        print("   方式2: 创建 config_secrets.json 文件")
        print("         {\"DASHSCOPE_API_KEY\": \"your-api-key\"}")
        exit(1)
    
    # 测试 1: bind_tools
    # test_bind_tools()
    
    # 测试 2: with_structured_output
    supports_structured = test_with_structured_output()
    
    # 测试 3: 如果不支持，测试手动实现
    # if not supports_structured:
    #     print("\n⚠️  with_structured_output 不支持，使用手动实现")
    #     test_manual_implementation()