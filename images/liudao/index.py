from airtest.core.api import Template

data = {
    "entry": Template(
        r"tpl1695858534837.png", record_pos=(0.383, 0.176), resolution=(2700, 1228)
    ),
    "entry_confirm": Template(
        r"tpl1695858548693.png", record_pos=(-0.236, 0.165), resolution=(2700, 1228)
    ),
    "entry_attack": Template(
        r"tpl1695858801698.png", record_pos=(0.382, 0.168), resolution=(2700, 1228)
    ),
    "entry_attack_in": Template(
        r"tpl1696231474587.png", record_pos=(0.385, 0.176), resolution=(2532, 1170)
    ),
    "btn_confirm": Template(
        r"tpl1695858586279.png", record_pos=(0.337, 0.167), resolution=(2700, 1228)
    ),
    "btn_confirm_b": Template(
        r"tpl1695858593290.png", record_pos=(-0.2, 0.134), resolution=(2700, 1228)
    ),
    "success_gift": Template(
        r"tpl1695858881087.png", record_pos=(0.002, -0.127), resolution=(2700, 1228)
    ),
    "back": Template(
        r"tpl1695858888789.png", record_pos=(-0.432, -0.202), resolution=(2700, 1228)
    ),
    "back_confirm": Template(
        r"tpl1695858896112.png", record_pos=(0.062, -0.011), resolution=(2700, 1228)
    ),
    "attack_target": Template(
        r"tpl1695858768815.png", record_pos=(0.15, 0.02), resolution=(2700, 1228)
    ),
    "guanka_aozhan": Template(
        r"tpl1695858626596.png",
        threshold=0.4,
        record_pos=(0.054, 0.025),
        resolution=(2700, 1228),
    ),
    "attack_iden": Template(
        r"tpl1695962168900.png",
        record_pos=(0.061, -0.076),
        resolution=(2700, 1228),
        threshold=0.85,
    ),
    # 椒图
    "wanfaxiangqing": Template(
        r"tpl1695898646337.png", record_pos=(0.289, 0.182), resolution=(2532, 1170)
    ),
    "shishenlu": Template(
        r"tpl1695899810784.png", record_pos=(0.349, 0.077), resolution=(2532, 1170)
    ),
    "beizhan": Template(
        r"tpl1695900579388.png", record_pos=(-0.415, 0.195), resolution=(2532, 1170)
    ),
    "attack_target": Template(
        r"tpl1695903081953.png",
        threshold=0.4,
        record_pos=(-0.198, 0.095),
        resolution=(2532, 1170),
    ),
    # 椒图关卡
    # aozhan
    "guanka_hundun": Template(
        r"tpl1695903529863.png", record_pos=(0.015, 0.064), resolution=(2532, 1170)
    ),
    "guanka_xingzhiyu": Template(
        r"tpl1695903618433.png", record_pos=(0.012, 0.055), resolution=(2532, 1170)
    ),
    "guanka_shenmi": Template(
        r"tpl1695903662098.png", record_pos=(0.055, 0.042), resolution=(2532, 1170)
    ),
    "guanka_ningxi": Template(
        r"tpl1695903669978.png",
        # threshold=0.6,
        record_pos=(-0.218, -0.008),
        resolution=(2532, 1170),
    ),
    "attack_jingying": Template(
        r"tpl1696232114646.png",
        threshold=0.85,
        record_pos=(-0.003, -0.08),
        resolution=(2532, 1170),
    ),
    "icon_buff": Template(
        r"tpl1696254840497.png",
        record_pos=(0.079, -0.092),
        resolution=(2532, 1170),
    ),
    "icon_buff_small": Template(
        r"tpl1696256016050.png",
        record_pos=(0.316, -0.139),
        resolution=(2532, 1170),
        threshold=0.35,
        rgb=True,
    ),
    "btn_move": Template(
        r"tpl1696256428360.png", record_pos=(0.406, 0.166), resolution=(2532, 1170)
    ),
    "btn_cancel": Template(
        r"tpl1698484877742.png", record_pos=(-0.092, 0.055), resolution=(2208, 1242)
    ),
    "btn_fangzao": Template(
        r"tpl1696256552380.png", record_pos=(0.404, 0.189), resolution=(2532, 1170)
    ),
    "guanka_boss": Template(
        r"tpl1696390028555.png", record_pos=(0.007, -0.094), resolution=(2532, 1170)
    ),
    "boss_gift": Template(
        filename="tpl1695623958058.png",
        threshold=0.9,
        record_pos=(-0.18, -0.041),
        resolution=(2700, 1228),
    ),
    "btn_refresh": Template(
        r"tpl1696396460269.png", record_pos=(0.41, 0.182), resolution=(2532, 1170)
    ),
}
