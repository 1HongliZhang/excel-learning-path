# VBA 宏与自动化

## 一、VBA 基础

### 1.1 什么是 VBA

VBA（Visual Basic for Applications）是 Excel 的宏语言，可以：
- 自动化重复任务
- 创建自定义功能
- 操作工作表和单元格
- 创建用户界面

### 1.2 打开 VBA 编辑器

**方法一：快捷键**
- `Alt+F11`：打开 VBA 编辑器

**方法二：开发工具选项卡**
1. 「开发工具」选项卡 →「Visual Basic」
2. 如果没有「开发工具」选项卡：
   - 「文件」→「选项」→「自定义功能区」
   - 勾选「开发工具」
   - 点击「确定」

### 1.3 VBA 编辑器界面

**主要窗口**：
- **工程资源管理器**：显示工作簿和模块
- **属性窗口**：显示选中对象的属性
- **代码窗口**：编写和编辑 VBA 代码
- **立即窗口**：调试和测试代码

## 二、录制宏

### 2.1 录制宏的步骤

**操作步骤**：
1. 「开发工具」选项卡 →「录制宏」
2. 在弹出的对话框中：
   - 输入宏名称（不能有空格）
   - 选择保存位置（个人宏工作簿/当前工作簿）
   - 输入快捷键（可选）
   - 输入说明（可选）
3. 点击「确定」
4. 执行要自动化的操作
5. 点击「停止录制」

### 2.2 录制宏的注意事项

**优点**：
- 无需编程知识
- 快速创建宏
- 自动生成代码

**缺点**：
- 代码冗余
- 缺乏灵活性
- 可能录制不必要的步骤

### 2.3 编辑录制的宏

**操作步骤**：
1. `Alt+F11` 打开 VBA 编辑器
2. 在工程资源管理器中找到录制的宏
3. 双击打开代码窗口
4. 修改代码
5. 按 `F5` 运行宏

## 三、VBA 基本语法

### 3.1 变量声明

**声明变量**：
```vba
Dim 变量名 As 数据类型
```

**常用数据类型**：
```vba
Dim name As String       ' 字符串
Dim age As Integer       ' 整数
Dim salary As Double     ' 双精度浮点数
Dim isActive As Boolean  ' 布尔值
Dim ws As Worksheet      ' 工作表对象
Dim rng As Range         ' 单元格区域对象
```

**隐式声明**：
- 不声明类型，默认为 Variant 类型
- 不推荐使用

### 3.2 常量声明

```vba
Const PI As Double = 3.14159
Const COMPANY_NAME As String = "ABC公司"
```

### 3.3 条件语句

**If 语句**：
```vba
If 条件 Then
    ' 执行语句
ElseIf 条件 Then
    ' 执行语句
Else
    ' 执行语句
End If
```

**Select Case 语句**：
```vba
Select Case 变量
    Case 值1
        ' 执行语句
    Case 值2
        ' 执行语句
    Case Else
        ' 执行语句
End Select
```

### 3.4 循环语句

**For 循环**：
```vba
For i = 1 To 10
    ' 执行语句
Next i

For Each cell In Range("A1:A10")
    ' 执行语句
Next cell
```

**Do 循环**：
```vba
Do While 条件
    ' 执行语句
Loop

Do Until 条件
    ' 执行语句
Loop
```

### 3.5 过程与函数

**Sub 过程**：
```vba
Sub 过程名()
    ' 执行语句
End Sub
```

**Function 函数**：
```vba
Function 函数名(参数 As 类型) As 返回类型
    ' 执行语句
    函数名 = 返回值
End Function
```

## 四、操作工作表和单元格

### 4.1 引用工作表

```vba
' 通过名称引用
Worksheets("Sheet1").Select

' 通过索引引用
Worksheets(1).Select

' 设置变量
Dim ws As Worksheet
Set ws = Worksheets("销售数据")
```

### 4.2 引用单元格

```vba
' 引用单个单元格
Range("A1").Value = "Hello"
Cells(1, 1).Value = "Hello"

' 引用区域
Range("A1:C10").Select
Range("A1:C10").Copy

' 动态引用
Range("A1").End(xlDown).Select
Range("A1").CurrentRegion.Select
```

### 4.3 读写单元格值

```vba
' 读取值
Dim val As Variant
val = Range("A1").Value

' 写入值
Range("B1").Value = 100
Range("C1").Value = "文本"
Range("D1").Value = Date
```

### 4.4 设置单元格格式

```vba
' 设置字体
Range("A1").Font.Name = "宋体"
Range("A1").Font.Size = 12
Range("A1").Font.Bold = True
Range("A1").Font.Color = RGB(255, 0, 0)

' 设置对齐方式
Range("A1").HorizontalAlignment = xlCenter
Range("A1").VerticalAlignment = xlTop

' 设置填充颜色
Range("A1").Interior.Color = RGB(255, 255, 0)

' 设置边框
Range("A1:C10").Borders.LineStyle = xlContinuous
Range("A1:C10").Borders.Color = RGB(0, 0, 0)
```

## 五、示例练习

### 5.1 格式化报表

**场景**：自动格式化销售报表

**操作步骤**：
1. 录制宏，执行格式化操作
2. 编辑代码，优化冗余步骤
3. 运行宏

**代码示例**：
```vba
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = Worksheets("销售报表")
    
    ' 设置标题格式
    ws.Range("A1:F1").Font.Bold = True
    ws.Range("A1:F1").Font.Size = 14
    ws.Range("A1:F1").HorizontalAlignment = xlCenter
    ws.Range("A1:F1").Interior.Color = RGB(0, 102, 204)
    ws.Range("A1:F1").Font.Color = RGB(255, 255, 255)
    
    ' 设置数据区域格式
    ws.Range("A2:F100").Font.Size = 11
    ws.Range("A2:F100").HorizontalAlignment = xlCenter
    
    ' 设置货币格式
    ws.Range("E2:E100").NumberFormat = "¥#,##0.00"
    
    ' 自动调整列宽
    ws.Columns("A:F").AutoFit
    
    ' 冻结首行
    ws.Range("A2").Select
    ws.Activate
    ActiveWindow.FreezePanes = True
    
    MsgBox "报表格式化完成！"
End Sub
```

### 5.2 批量重命名工作表

**场景**：按指定模式重命名所有工作表

**代码示例**：
```vba
Sub RenameSheets()
    Dim i As Integer
    Dim ws As Worksheet
    
    i = 1
    For Each ws In Worksheets
        ws.Name = "Sheet" & i
        i = i + 1
    Next ws
    
    MsgBox "工作表重命名完成！"
End Sub
```

### 5.3 数据验证

**场景**：批量添加数据验证规则

**代码示例**：
```vba
Sub AddDataValidation()
    Dim ws As Worksheet
    Set ws = Worksheets("员工信息")
    
    ' 添加下拉列表
    With ws.Range("C2:C100").Validation
        .Delete
        .Add Type:=xlValidateList, _
             AlertStyle:=xlValidAlertStop, _
             Operator:=xlBetween, _
             Formula1:="销售部,技术部,人事部,财务部"
        .IgnoreBlank = True
        .InCellDropdown = True
    End With
    
    ' 添加数值限制
    With ws.Range("D2:D100").Validation
        .Delete
        .Add Type:=xlValidateDecimal, _
             AlertStyle:=xlValidAlertStop, _
             Operator:=xlBetween, _
             Formula1:=4000, _
             Formula2:=50000
        .IgnoreBlank = True
    End With
    
    MsgBox "数据验证添加完成！"
End Sub
```

### 5.4 创建用户表单

**场景**：创建简单的数据录入表单

**操作步骤**：
1. 打开 VBA 编辑器
2. 「插入」→「用户窗体」
3. 添加控件（标签、文本框、按钮）
4. 编写按钮点击事件代码
5. 运行用户表单

**代码示例**：
```vba
Private Sub CommandButton1_Click()
    Dim ws As Worksheet
    Dim lastRow As Long
    
    Set ws = Worksheets("数据录入")
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row + 1
    
    ws.Cells(lastRow, "A").Value = TextBox1.Value  ' 姓名
    ws.Cells(lastRow, "B").Value = TextBox2.Value  ' 部门
    ws.Cells(lastRow, "C").Value = TextBox3.Value  ' 薪资
    
    TextBox1.Value = ""
    TextBox2.Value = ""
    TextBox3.Value = ""
    
    MsgBox "数据录入成功！"
End Sub

Private Sub CommandButton2_Click()
    Unload Me
End Sub
```

## 六、运行和调试宏

### 6.1 运行宏

**方法一：快捷键**
- `Alt+F8`：打开宏对话框
- 选择要运行的宏
- 点击「执行」

**方法二：VBA 编辑器**
- 打开包含宏的代码窗口
- 按 `F5` 运行

**方法三：按钮**
1. 「开发工具」→「插入」→「按钮（窗体控件）」
2. 绘制按钮
3. 在弹出的对话框中选择要关联的宏
4. 点击「确定」

### 6.2 调试宏

**设置断点**：
1. 在代码窗口中点击行号左侧的灰色区域
2. 红色圆点表示断点
3. 运行宏时会在断点处暂停

**逐行执行**：
- `F8`：逐行执行
- `Shift+F8`：逐过程执行
- `Ctrl+Shift+F8`：跳出当前过程

**监视窗口**：
1. 「视图」→「监视窗口」
2. 添加要监视的变量或表达式
3. 运行宏时可以查看变量值

## 七、常见错误与技巧

### 7.1 常见错误

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| 宏无法运行 | 宏安全设置阻止 | 降低宏安全级别 |
| 运行时错误 '1004' | 对象引用错误 | 检查工作表/单元格引用 |
| 类型不匹配 | 数据类型错误 | 检查变量类型 |
| 下标越界 | 数组或集合引用错误 | 检查索引范围 |

### 7.2 实用技巧

1. **使用 Option Explicit**：强制变量声明，避免拼写错误
2. **使用 With 语句**：简化对象操作
3. **关闭屏幕更新**：提高宏运行速度
4. **错误处理**：使用 On Error Resume Next 或 On Error GoTo

---

**适用版本**：所有 Excel 版本
