# -*- coding: utf-8 -*-
"""PPT v3 深度讲义版组装器: 每课约44-51页"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ppt_gen_v3 import DeckV3                       # noqa: E402
import sessions_meta as SM                          # noqa: E402
import sessions_meta2 as SM2                        # noqa: E402
import meta3_ai, meta3_py, meta3_pp                 # noqa: E402
import universe as UNI                              # noqa: E402
from build_ppts import (COURSES, MARK, cn_week,     # noqa: E402
                        split_sessions, group_items, lesson_title,
                        goals_of, next_prev_of)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAT = os.path.join(BASE, "教学实施资料")

M3 = {"ai": meta3_ai.AI3, "py": meta3_py.PY3, "pp": meta3_pp.PP3}

POSITION = {
    "ai": [("课程性质", "专业核心能力进阶课：无代码体验→轻代码实现→工业级应用"),
           ("面向岗位", "AI应用工程师、工业视觉开发、工业互联网数据分析"),
           ("对接证书", "AI应用实践（中级）、工业互联网平台运维、计算机视觉工程师"),
           ("课程衔接", "前：无Python先修（零基础入门） → 本课(第4-11周，与Python基础并行) → 后：项目实战")],
    "py": [("课程性质", "专业核心基础课：面向零基础新生的编程第一课"),
           ("面向岗位", "工业数据采集技术员、边缘计算运维、平台运维员"),
           ("对接证书", "Python开发（工信部）、AI应用实践、企业应用实施工程师"),
           ("课程衔接", "前：计算机文化基础 → 本课(第1-12周) → 后：AI应用基础")],
    "pp": [("课程性质", "自包含工程应用课：C语言底子直接上工业项目"),
           ("面向岗位", "数据工程师、数据分析、AI应用、采集技术员"),
           ("对接证书", "Python开发、数据应用与服务（1+X）、AI应用实践"),
           ("课程衔接", "前置仅需C语言 → 本课(第1-8周) → 后：毕业设计/平台实习")],
}


def flow_fig_for(course, four):
    if four:
        return ("课堂教法四步法（每课时40分钟）",
                ["讲10min", "演10min", "模仿10min", "练习10min"],
                "PRIMM融合：预测→运行→研究→修改→创造")
    return ("六步法课堂化（资讯计划课前完成）",
            ["资讯·计划", "决策10", "实施一30", "检查5", "实施二25", "评价10"],
            "时间单位: 分钟（除标注外）｜合计80分钟")


def build_course(c):
    mod = __import__(c["mod"])
    outdir = os.path.join(MAT, c["folder"], "授课PPT")
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        fp = os.path.join(outdir, f)
        if os.path.isfile(fp):
            os.remove(fp)
    count = pages = 0
    for wi, week in enumerate(mod.WEEKS, 1):
        meta_key = wi + 3 if c["mod"] == "data_ai" else wi
        week_meta = c["meta"].get(meta_key)
        m3 = M3[c["code"]].get(meta_key)
        sessions = split_sessions(week)
        for si, (no, header, items) in enumerate(sessions):
            meta = week_meta if c["mod"] == "data_ai" else week_meta["tasks"][si]
            m2 = SM2.D.get((c["code"], meta_key, si), {})
            d = DeckV3()
            title = lesson_title(header, week)
            sub = f"第{cn_week(meta_key)}周 · 第{no}次课（2课时 · 80分钟）"
            illus = os.path.join(outdir, "_场景插画", f"W{meta_key}_场景.png")
            if not os.path.exists(illus):
                illus = None
            # ===== 第一部分 定位 =====
            from env_tools import tool_for
            _tp, _tg = tool_for(c["code"], meta_key)
            d.cover(c["name"], title, sub,
                    f"{c['place']}  ·  理实一体  ·  配套：分层工单+starter  ·  本课主用：{_tp}",
                    dept=UNI.DEPTS[c["code"]]["name"], illus=illus)
            # v9: 议程页（六部分+分钟归属，四步法周次换口径）
            four_agenda = wi in c["four_step_weeks"]
            AG = [("01", "课程定位", "课前已读", "性质·岗位·证书：为什么学这门课"),
                  ("02", "课堂流程", "约2′", "80分钟时间盒与ABCD分层节奏"),
                  ("03", "目标与资讯·情境", "约5′", "带着目标进课堂+两江智造本课剧情"),
                  ("04", "知识精讲", "约15′", "基础知识大卡+代码演示（先例后理）"),
                  ("05", "任务实施", "六步法核心", "工单发布·分层执行·避坑" ),
                  ("06", "检查与评价", "约15′", "三层质检·当堂评分·课后任务")]
            if four_agenda:
                AG = [("01", "课程定位", "课前已读", "性质·岗位·证书：为什么学这门课"),
                      ("02", "课堂流程", "约2′", "四步法节奏：讲-演-模仿-练习"),
                      ("03", "目标与资讯·情境", "约5′", "目标+两江智造本课剧情"),
                      ("04", "知识精讲", "讲10′+演10′", "基础知识大卡+现场演示"),
                      ("05", "模仿与练习", "10′+10′", "跟做保底→独立完成（工单分层）"),
                      ("06", "检查与评价", "约15′", "三层质检·当堂评分·课后任务")]
            d.note(f"开场30秒：本次课《{title}》，80分钟＝2课时×40分钟。"
                   "课前已发工单+starter+微课知识卡，资讯·计划线上完成。")
            d.agenda(AG, tail="资讯·计划已于课前线上完成——课堂从决策/演示直接开始")
            d.note("议程页30秒：指读六个部分的分钟归属，强调'资讯计划课前已完成'；"
                   "告诉学生'每次课都知道现在在哪一步、还剩多少时间'。")
            d.section("01", "课程定位", "本课在课程体系中的位置（课程标准摘录）")
            d.note("过渡页：一句话点明本部分——先明确这门课'为什么学、学了去哪'。")
            d.positioning(c["name"], POSITION[c["code"]])
            d.note("念'课程性质'一行即可，重点指读'对接证书'与'课程衔接'，"
                   "让学生知道本课与前后课程的关系（30秒）。")
            d.mindmap(title[:8], [
                ("基础知识", m3["basics"][:2]),
                ("继续夯实", m3["basics"][2:4]),
                ("技能点", m3["skills"][:2]),
                ("分层任务", ["D跟做保底", "C基础完成", "B标准达成", "A进阶拓展"]),
                ("课堂评价", ["功能40%", "技术25%", "规范20%", "素养15%"]),
            ])
            d.note("知识地图：先见森林后见树木。指着四条分支预告本课路线，"
                   "不展开细讲（40秒）。")
            # ===== 第二部分 流程 =====
            d.section("02", "课堂流程", "80分钟时间盒与个人节奏")
            d.note("流程预告：强调'资讯·计划已在课前完成'，课堂从决策直接开始。")
            four = wi in c["four_step_weeks"]
            from sessions_meta import FOUR, SIX
            d.flow(FOUR if four else SIX,
                   "每课时40分钟 · 共80分钟（四步法）" if four
                   else "每课时40分钟 · 共80分钟（六步法课堂化）")
            d.note("讲10→演10→模仿10→练习10" if four else
                   "决策10→实施30→检查5→实施25→评价10；评价环节不压缩")
            d.pace()
            d.note("分层节奏：D层跟做保底、C层基础完成、B层标准达成、A层进阶拓展；"
                   "每人按工单勾选自己的层，每4周动态升降。")
            # ===== 第三部分 目标与资讯 =====
            d.section("03", "目标与资讯", "带着目标进课堂（Predict·预测）")
            d.note("PRIMM的Predict：先让学生猜，再揭晓。")
            d.goals(goals_of(week))
            d.note("目标解读：点读1-2个关键动词（能编写/能诊断/能部署），"
                   "说明这就是今天工单的验收口径。")
            d.review(meta["quiz"], c["chk"])
            d.note("课前测讲评：随机点2名学生说答案，只追问'为什么'，不展开讲；"
                   "错得多的题记到'检查'环节再回收。")
            d.practice(1, meta["quiz"],
                       m2.get("cautions", ["先自己想30秒再讨论"])[0])
            d.note("快问快答：同桌互问30秒，举手表决；答案不公布，留到知识精讲验证。")
            scen = UNI.SCEN.get((c["code"], meta_key))
            if scen:
                d.scenario(scen, dept=UNI.DEPTS[c["code"]]["name"], illus=illus)
            else:
                d.scenario(meta["sc"] or title)
            d.note(f"情境说书（30秒，口头讲，不必逐字念）：{scen or meta['sc']}\n"
                   "讲完抛出问题：'如果是你，第一步先干什么？'——自然过渡到决策环节。")
            # ===== 第四部分 知识精讲 =====
            d.section("04", "知识精讲", "基础知识 → 详解 → 技能 → 代码")
            d.note("知识精讲开始：每条知识对应一张大卡，讲法'先例后理'。")
            b = m3["basics"]
            for bi, bt in enumerate(b, 1):
                d.basic_card(bi, bt)
                d.note(f"知识卡{bi}：{bt}\n"
                       "讲法：先给一个车间/产线的例子，再给定义；"
                       "讲完随机点1名学生用自己的话复述（每个30-60秒，控制节奏）。")
            d.quick_check(b[:5])
            d.note("快查核对：遮住左栏让学生说右栏含义；全对的小组加过程分。")
            if m2.get("kn"):
                d.knowledge(0, m2["kn"])
                d.note("深化讲解：面向A/B层的进阶理解，C/D层听懂结论即可。")
            d.skills(m3["skills"])
            d.note("技能点＝今天'做完你应该会'，逐条对应工单步骤与评分点。")
            if c["code"] == "ai":
                d.metrics_card()
            groups = group_items(items)
            dcur, lines, slide_no = [], 0, 1

            def flush():
                nonlocal slide_no
                if dcur:
                    flat = [("· " + t) if sub else t for t, sub in dcur]
                    d.content(slide_no, f"{title}（{slide_no}）", flat)
                    slide_no += 1
                    d.note("实施内容清单：本页条目与工单步骤一一对应，"
                           "逐项过一遍即可，细节留到代码演示。")
            for parent, subs in groups:
                est = 1 + len(subs)
                if lines + est > 8 and dcur:
                    flush()
                    dcur, lines = [], 0
                dcur.append((parent, False))
                lines += 1
                for s_ in subs:
                    dcur.append((s_, True))
                    lines += 1
            flush()
            for ct, cc in m3["code"][:2]:
                d.code(ct, cc)
                d.note(f"现场演示《{ct}》：三步走——先整段跑通看结果，"
                       "再逐行讲关键语句，最后现场改一个参数看输出变化（演10分钟的核心素材）。")
            ft, fsteps, fnote = flow_fig_for(c["code"], four)
            d.fig_flow(ft, fsteps, fnote)
            d.note("流程图页：可快速带过，作为'我们现在在哪一步'的路标。")
            from pptx.dml.color import RGBColor as _RC
            d.fig_bars("80分钟时间盒分配（分钟）",
                       [("决策", 10, _RC(0x05, 0x45, 0xE8)),
                        ("实施一", 30, _RC(0x04, 0x75, 0xB6)),
                        ("检查", 5, _RC(0xF5, 0x67, 0x0F)),
                        ("实施二", 25, _RC(0x01, 0x75, 0x1F)),
                        ("评价", 10, _RC(0x44, 0x54, 0x6A))], ymax=30,
                       note="评价环节不压缩：10分钟当堂评分+24小时反馈")
            d.note("强调柱状图最右两根：实施二25分钟是冲优秀的时间，"
                   "评价10分钟不压缩——当堂评分、24小时内反馈。")
            if meta_key in (12, 8) and c["code"] == "py" or (c["code"] == "pp" and meta_key == 8):
                d.fig_arch("综合系统架构（分层）", [
                    ("展示层", ["仪表盘", "PDF报告"]),
                    ("分析层", ["阈值检测", "统计聚合"]),
                    ("数据层", ["清洗管道", "SQLite"]),
                    ("采集层", ["Modbus", "文件/模拟"])])
                d.note("架构分层讲解：自下而上过一遍数据流向，"
                       "答辩时按此图讲'系统架构'。")
            # ===== 第五部分 任务实施 =====
            d.section("05", "任务实施", "工单 · 分层 · 步骤 · 避坑")
            d.note("进入实施：先决策、再领工单、按层执行。")
            dec = meta["dec"]
            d.decision(dec["title"], dec["header"], dec["rows"],
                       dec.get("note", ""))
            d.note("决策矩阵用法（10分钟）：组内对备选方案打分→选型→把结论和理由"
                   "写进工单'决策记录'栏；教师抽查2组口头说理由（决策追责）。")
            d.task(meta["wono"], meta["woname"], meta["steps"],
                   meta["sp"], meta["sg"])
            d.note(f"工单发布话术：'{UNI.DEPTS[c['code']]['name']}发来工单"
                   f"{meta['wono']}《{meta['woname']}》，及格线是{meta['sp'][0]}，"
                   "优秀线看A层标准'——念完发starter。")
            extA = m2.get("extA", "在优秀基础上完成创新优化")
            tier_note = {
                "D": "D层·学徒：跟做保底。教师或屏幕领做，做完即达标，绝不留白。",
                "C": "C层·操作员：基础完成。按工单步骤独立完成，卡壳先查错误速查表。",
                "B": "B层·组长：标准达成。全部功能+规范，完成后帮带同组D/C层。",
                "A": "A层·师傅：进阶拓展。完成拓展任务并准备2分钟展示；费曼式讲给D层听。",
            }
            for tier in "DCBA":
                t = m3["abcd"][tier]
                d.tier_detail(tier, t["goal"], t["steps"], t["std"],
                              extA if tier == "A" else None)
                d.note(tier_note[tier])
            d.steps_caution(meta["steps"], m2.get("cautions",
                                                  ["按工单避坑清单执行"]))
            d.note("避坑清单：每条问'为什么会踩'，点名学生解释，"
                   "把'注意'变成'知道为什么注意'。")
            d.errors(m3["errors"])
            e0 = m3["errors"][0]
            d.note(f"错误速查：现场演示第一条——制造「{e0[0]}」，带着学生按'现象→原因→解决'三步排查。")
            d.practice(2, f"运行时出现「{e0[0]}」，你的排查顺序是？",
                       f"提示: 原因是{e0[1]}")
            d.note("先让学生说排查顺序再给提示：训练'看报错信息'的条件反射。")
            # ===== 第六部分 检查评价 =====
            d.section("06", "检查与评价", "三层质检 · 评分 · 课后")
            d.note("收尾5分钟检查+10分钟评价。")
            d.check()
            d.note("三层质检组织：自查明细→同伴互查（签字）→教师抽查2组；"
                   "查出的缺陷当场修，修不完记入课后任务。")
            d.submission(meta["wono"])
            d.note("提交强调：文件命名'学号_姓名_工单号.zip'，24小时内教师在平台反馈评分。")
            d.closing_tasks(week["homework"], next_prev_of(week["homework"]))
            d.note("课后任务逐条念，说明下次课的衔接关系；预告下次课前微课与导学单。")
            # 37号轮：教材预习/检查知识点入演讲者备注（不占正文版面）
            _tb = week.get("textbook", [])
            if _tb:
                d.note("教材衔接：" + " | ".join(_tb))
            d.literacy(LITERACY[c["code"]])
            d.note("素养页：结合本课内容点一个真实案例（如数据脱敏、代码抄袭后果），30秒即可。")
            d.shot_placeholder()
            d.note("提醒：运行截图/实拍照片贴到工单过程记录栏，作为过程性考核证据。")
            d.thanks()
            d.note("下课提醒：关机→椅归位→带走工单；教师课后24h内完成反馈。")
            try:
                nw = c["meta"].get(meta_key + 1)
                nm3 = M3[c["code"]].get(meta_key + 1)
                if nw and nm3:
                    q = nw["quiz"] if c["mod"] == "data_ai" else nw["tasks"][0]["quiz"]
                    d.preview(next_title(c, meta_key + 1), q, meta_key + 1)
                    d.note("下次课预告：布置课前微课知识卡与导学单，形成学习闭环。")
            except Exception:
                pass
            from ppt_gen_v3 import _decorate
            _decorate(d, c["name"])
            fname = f"W{meta_key:02d}-第{no}次课-{title[:14]}.pptx"
            d.save(os.path.join(outdir, fname))
            count += 1
            pages += len(d.prs.slides._sldIdLst)
    print(f"{c['name']}: {count}个PPT, 平均{pages // max(count, 1)}页/课 → {outdir}")


LITERACY = {
    "ai": ["模型可解释与数据伦理：不迷信黑盒, 尊重隐私与合规红线",
           "工程化思维：从模型精度到系统可用, 版本可管理、结果可复现",
           "持续学习：追踪大模型前沿, 用工单沉淀个人知识资产"],
    "py": ["工匠精神：规范命名、及时保存、报错必究的编码习惯",
           "工程伦理：数据安全与隐私保护, 不抄代码、引用注明",
           "协作素养：ABCD角色轮换履职, 贡献表如实填报"],
    "pp": ["工程责任：代码可维护、文档完整、测试先行",
           "绿色计算：向量化省算力, 批量写入降开销",
           "职业规划：以项目档案袋对接岗位与竞赛"],
}


def next_title(c, wk):
    mod = __import__(c["mod"])
    m3 = M3[c["code"]].get(wk)
    if m3:
        return m3["skills"][0][:24]
    return "见下次课工单"


if __name__ == "__main__":
    for c in COURSES:
        build_course(c)


