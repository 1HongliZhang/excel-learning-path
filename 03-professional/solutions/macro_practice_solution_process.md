# macro_practice.xlsm 练习解决方案

## 练习目标

1. 录制宏完成报表格式化
2. 编辑和优化宏代码
3. 编写 VBA 代码计算销售额
4. 运行和调试宏

## 数据说明

该文件包含销售数据：
- 日期：销售日期
- 产品：产品名称
- 区域：销售区域
- 销售量：销售数量
- 单价：产品单价
- 销售额：空白，需要计算

## 解决方案步骤

### Step 1: 启用开发工具选项卡

**操作步骤**：
1. 「文件」选项卡 →「选项」→「自定义功能区」
2. 在右侧列表中勾选「开发工具」
3. 点击「确定」

### Step 2: 录制格式化宏

**操作步骤**：
1. 「开发工具」选项卡 →「录制宏」
2. 在弹出的对话框中：
   - 宏名称：FormatReport
   - 保存位置：当前工作簿
   - 快捷键：Ctrl+Shift+F
   - 点击「确定」
3. 执行以下操作：
   - 选中 A1:F1 区域
   - 设置字体为粗体，字号为14，居中对齐
   - 设置背景色为蓝色（RGB(0,102,204)），字体颜色为白色
   - 选中 A2:F51 区域，设置字号为11，居中对齐
   - 设置 E2:E51 为货币格式（¥#,##0.00）
   - 设置 F2:F51 为货币格式（¥#,##0.00）
   - 自动调整列宽
   - 冻结首行
4. 点击「停止录制」

### Step 3: 编辑宏代码

**操作步骤**：
1. `Alt+F11` 打开 VBA 编辑器
2. 在工程资源管理器中找到「FormatReport」宏
3. 双击打开代码窗口
4. 优化代码，去除冗余步骤

**优化后的代码**：
```vba
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    
    With ws
        .Range("A1:F1").Font.Bold = True
        .Range("A1:F1").Font.Size = 14
        .Range("A1:F1").HorizontalAlignment = xlCenter
        .Range("A1:F1").Interior.Color = RGB(0, 102, 204)
        .Range("A1:F1").Font.Color = RGB(255, 255, 255)
        
        .Range("A2:F51").Font.Size = 11
        .Range("A2:F51").HorizontalAlignment = xlCenter
        
        .Range("E2:F51").NumberFormat = "¥#,##0.00"
        
        .Columns("A:F").AutoFit
        
        .Range("A2").Select
        .Activate
        ActiveWindow.FreezePanes = True
    End With
    
    MsgBox "报表格式化完成！"
End Sub
```

### Step 4: 编写计算销售额的宏

**操作步骤**：
1. 在 VBA 编辑器中插入新模块
2. 编写以下代码：

```vba
Sub CalculateSales()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long
    
    Set ws = Worksheets("Sheet1")
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    
    For i = 2 To lastRow
        ws.Cells(i, "F").Value = ws.Cells(i, "D").Value * ws.Cells(i, "E").Value
    Next i
    
    MsgBox "销售额计算完成！"
End Sub
```

### Step 5: 编写综合宏

**操作步骤**：
1. 在 VBA 编辑器中编写以下代码：

```vba
Sub RunAll()
    CalculateSales
    FormatReport
End Sub
```

### Step 6: 运行宏

**方法一：快捷键**
1. `Alt+F8` 打开宏对话框
2. 选择要运行的宏（如 RunAll）
3. 点击「执行」

**方法二：按钮**
1. 「开发工具」→「插入」→「按钮（窗体控件）」
2. 在工作表上绘制按钮
3. 在弹出的对话框中选择「RunAll」宏
4. 点击「确定」
5. 右键按钮，编辑文字为「运行报表」

### Step 7: 调试宏

**设置断点**：
1. 在代码窗口中点击行号左侧的灰色区域
2. 红色圆点表示断点
3. 运行宏时会在断点处暂停

**逐行执行**：
- `F8`：逐行执行
- 观察立即窗口中的变量值

## 最终效果

完成后的工作簿应包含：
- 三个宏：FormatReport、CalculateSales、RunAll
- 计算完成的销售额列
- 格式化好的报表样式
- 一个「运行报表」按钮

## 常见问题与解决方案

| 问题 | 原因 | 解决方法 |
|------|------|----------|
| 宏无法运行 | 宏安全设置阻止 | 降低宏安全级别 |
| 运行时错误 '1004' | 对象引用错误 | 检查工作表/单元格引用 |
| 类型不匹配 | 数据类型错误 | 检查变量类型 |
| 宏运行慢 | 屏幕更新频繁 | 添加 `Application.ScreenUpdating = False` |

## 优化技巧

1. **关闭屏幕更新**：
   ```vba
   Application.ScreenUpdating = False
   ' 代码
   Application.ScreenUpdating = True
   ```

2. **禁用事件**：
   ```vba
   Application.EnableEvents = False
   ' 代码
   Application.EnableEvents = True
   ```

3. **使用 With 语句**：简化对象操作

4. **错误处理**：
   ```vba
   On Error Resume Next
   ' 代码
   On Error GoTo 0
   ```
