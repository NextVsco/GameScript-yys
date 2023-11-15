import os
import utils.index as util
from airtest.core.api import Template
import images.liudao.index as liudao

data = {
    "tansuo": "tpl1681175817312.png",
    "close": "tpl1681544499213.png",
    "msg_retract": "tpl1681531711439.png",
    "xiezuo_close": "tpl1680770938946.png",
    "xiezuo_refuse": "tpl1680692024341.png",
    # 战斗场景
    "fight_prepare": "tpl1680752782383.png",
    "fight_back": "tpl1680779890228.png",
    "fight_back_confirm": "tpl1685350758220.png",
    "fight_buff": "tpl1680778603986.png",
    "fight_fail": "tpl1680778828182.png",
    "fight_fail_attack": "tpl1685350908993.png",
    "fight_fail_attack_confirm": "tpl1680778399638.png",
    "A_fight_fail_attack_confirm": "tpl1686048296786.png",
    "fight_success": "tpl1689905383317.png",
    "fight_reward": "tpl1685414993017.png",
    # 御魂
    "yuhun": "tpl1679800091641.png",
    "yuhun_dashe1": "tpl1679800180459.png",
    "yuhun_dashe2": "tpl1679800240566.png",
    "yuhun_group_entry": "tpl1689903471828.png",
    "yuhun_group_team": "tpl1691758748842.png",
    # 突破
    "tupo_entry": "tpl1680749147597.png",
    "tupo_head": "tpl1680749252876.png",
    "tupo_target": "tpl1680774972269.png",
    "tupo_target_stop": "tpl1680775074386.png",
    "tupo_target_pass": "tpl1680754918941.png",
    "tupo_refresh": "tpl1680760859170.png",
    "tupo_confirm": "tpl1680778399638.png",
    "tupo_attack": "tpl1685350449338.png",
    "tupo_close": "tpl1680762259370.png",
    "tupo_reward": "tpl1680752561676.png",
    # 探索
    "tansuo_monster_boss": "tpl1681177394695.png",
    "tansuo_monster": "tpl1681177433604.png",
    "tansuo_iden": "tpl1681177539477.png",
    "tansuo_reward": "tpl1680696148840.png",
    "tansuo_back": "tpl1680696712522.png",
    "tansuo_back_confirm": "tpl1680696776178.png",
    "tansuo_reward_box": "tpl1681202853848.png",
    "tansuo_entry": "tpl1680780768585.png",
    "tansuo_entry_2": "tpl1680782341978.png",
    # 其他
    "other_yuling_entry2": "tpl1688272139192.png",
    "other_act_yuan": "tpl1690409785403.png",
    "other_confirm": "tpl1688221561656.png",
    # buff
    "buff_entry": "tpl1688784385359.png",
    "buff_open": "tpl1688783185895.png",
    "buff_exp": "tpl1688783236876.png",
    "buff_state_open": "tpl1693883296333.png",
}

dataAttr = {
    "fight_fail": {
        "threshold": 0.9,
        "record_pos": (-0.131, -0.147),
        "resolution": (2208, 1242),
    },
    "fight_fail_attack_confirm": {
        "record_pos": (0.064, 0.041),
        "threshold": 0.7,
        "resolution": (2208, 1242),
    },
}

dataInfo = {
    # 左下角式神血量条位置
    "tupo_our_main": Template(
        filename="tpl1691142140500.png",
        threshold=0.6,
        rgb=True,
        record_pos=(-0.317, 0.029),
        resolution=(2208, 1242),
    ),
    # yuhun 队友加号标识
    "yuhun_group_team": Template(
        filename="tpl1691758748842.png",
        record_pos=(0.288, -0.07),
        resolution=(2532, 1170),
    ),
    "yuhun_entry": Template(
        filename="tpl1679800091641.png",
        record_pos=(-0.338, 0.18),
        resolution=(2340, 1080),
    ),
    "yuhun_entry2": Template(
        filename="tpl1679800180459.png",
        record_pos=(-0.338, 0.18),
        resolution=(2340, 1080),
    ),
    "yuhun_ident": Template(
        filename="tpl1679800240566.png",
        record_pos=(-0.357, -0.1),
        resolution=(2340, 1080),
    ),
    "yuhun_entry_tu": Template(
        filename="tpl1679800269765.png",
        record_pos=(-0.202, 0.068),
        resolution=(2340, 1080),
    ),
    "yuhun_entry_wang": Template(
        filename="tpl1679800289301.png",
        record_pos=(-0.219, 0.138),
        resolution=(2340, 1080),
    ),
    # 队伍预设
    "team_shishenlu": Template(
        filename="tpl1695089244956.png",
        record_pos=(-0.425, -0.211),
        resolution=(2700, 1228),
    ),
    "team_yushe": Template(
        filename="tpl1695089254079.png",
        record_pos=(-0.358, -0.213),
        resolution=(2700, 1228),
    ),
    "team_group": Template(
        filename="tpl1695089265690.png",
        record_pos=(-0.215, -0.167),
        resolution=(2700, 1228),
    ),
    "team_group2": Template(
        filename="tpl1695089272777.png",
        record_pos=(0.32, -0.153),
        resolution=(2700, 1228),
    ),
    "team_back": Template(
        filename="tpl1695089240180.png",
        record_pos=(0.171, -0.123),
        resolution=(2700, 1228),
    ),
    "team_entry": Template(
        filename="tpl1681177525637.png",
    ),
    "tansuo_iden_lunhuan": Template(
        filename="tpl1695298406140.png",
        record_pos=(-0.408, 0.196),
        resolution=(2700, 1228),
    ),
    # 御灵
    "other_yuling_entry": Template(
        filename="tpl1688192349819.png",
        record_pos=(0.386, 0.157),
        resolution=(2700, 1228),
    ),
    # 活动
    "action_entry": Template(
        filename="tpl1695176630636.png",
        record_pos=(0.386, 0.157),
        resolution=(2700, 1228),
    ),
    "action_fight_success": Template(
        filename="tpl1695177181395.png",
        threshold=0.85,
        record_pos=(-0.179, -0.039),
        resolution=(2700, 1228),
    ),
    "action_entry1": Template(
        filename="tpl1695523159219.png",
        record_pos=(-0.112, -0.028),
        resolution=(2700, 1228),
    ),
    "action_entry2": Template(
        filename="tpl1695523145463.png",
        record_pos=(0.251, -0.041),
        resolution=(2700, 1228),
    ),
    "action_entry3": Template(
        filename="tpl1695177986519.png",
        record_pos=(0.244, -0.108),
        resolution=(2700, 1228),
    ),
    ### 破晓时分
    "action_px_entry1": Template(
        filename="tpl1695624801887.png",
        record_pos=(-0.29, 0.034),
        resolution=(2700, 1228),
    ),
    "action_px_entry2": Template(
        filename="tpl1695624819022.png",
        record_pos=(0.0, 0.148),
        resolution=(2700, 1228),
    ),
    "action_px_entry": Template(
        filename="tpl1695622882314.png",
        record_pos=(0.398, 0.164),
        resolution=(2700, 1228),
    ),
    "action_px_btn_choose": Template(
        filename="tpl1695622898009.png",
        record_pos=(-0.0, 0.157),
        resolution=(2700, 1228),
    ),
    "action_px_btn_jinghua": Template(
        filename="tpl1695623066607.png",
        record_pos=(-0.001, 0.189),
        resolution=(2700, 1228),
    ),
    "action_px_user": Template(
        filename="tpl1695624040788.png",
        record_pos=(-0.003, 0.124),
        resolution=(2700, 1228),
    ),
    "action_px_iden_combat": Template(
        filename="tpl1695624408478.png",
        record_pos=(-0.294, -0.208),
        resolution=(2700, 1228),
    ),
    "action_px_buff": Template(
        filename="tpl1695622909737.png",
        record_pos=(-0.156, 0.042),
        resolution=(2700, 1228),
    ),
    "action_px_buff2": Template(
        filename="tpl1695694448391.png",
        threshold=0.8,
        record_pos=(-0.001, 0.034),
        resolution=(2700, 1228),
    ),
    "action_px_choose_shishen": Template(
        filename="tpl1695622939643.png",
        record_pos=(-0.032, 0.171),
        resolution=(2700, 1228),
    ),
    "action_px_icon_yingzhan": Template(
        filename="tpl1695623012338.png",
        record_pos=(0.006, -0.102),
        resolution=(2700, 1228),
    ),
    "action_px_icon_yiwu": Template(
        filename="tpl1695623405535.png",
        record_pos=(0.014, -0.09),
        resolution=(2700, 1228),
    ),
    "action_px_icon_store": Template(
        filename="tpl1695623519080.png",
        record_pos=(-0.191, -0.04),
        resolution=(2700, 1228),
    ),
    "action_px_icon_qiyu": Template(
        filename="tpl1695624204303.png",
        record_pos=(0.229, -0.031),
        resolution=(2700, 1228),
    ),
    "action_px_icon_suiji": Template(
        filename="tpl1695713371825.png",
        record_pos=(0.007, -0.091),
        resolution=(2700, 1228),
    ),
    "action_px_icon_liudao": Template(
        filename="tpl1695623191087.png",
        record_pos=(0.011, -0.101),
        resolution=(2700, 1228),
    ),
    "action_px_icon_boss": Template(
        filename="tpl1695624555888.png",
        record_pos=(0.008, -0.093),
        resolution=(2700, 1228),
    ),
    "action_px_zhunbei": Template(
        filename="tpl1695623031423.png",
        record_pos=(0.39, 0.151),
        resolution=(2700, 1228),
    ),
    "action_px_move": Template(
        filename="tpl1695623119868.png",
        record_pos=(0.411, 0.175),
        resolution=(2700, 1228),
    ),
    "action_px_move_back": Template(
        # 商店/六道
        filename="tpl1695623149059.png",
        threshold=0.9,
        record_pos=(0.203, 0.078),
        resolution=(2700, 1228),
    ),
    "action_px_success_huode": Template(
        filename="tpl1695623087921.png",
        record_pos=(-0.007, -0.111),
        resolution=(2700, 1228),
    ),
    "action_px_success_shengli": Template(
        filename="tpl1695623053653.png",
        record_pos=(-0.007, -0.062),
        resolution=(2700, 1228),
    ),
    "action_px_yiwu_iden1": Template(
        filename="tpl1695623450639.png",
        record_pos=(-0.089, 0.023),
        resolution=(2700, 1228),
    ),
    "action_px_yiwu_iden2": Template(
        filename="tpl1695623641766.png",
        record_pos=(0.093, 0.024),
        resolution=(2700, 1228),
    ),
    "action_px_boss_attack": Template(
        filename="tpl1695624592679.png",
        record_pos=(0.204, 0.094),
        resolution=(2700, 1228),
    ),
    "action_px_boss_gift": Template(
        filename="tpl1695623958058.png",
        record_pos=(-0.18, -0.041),
        resolution=(2700, 1228),
    ),
    "action_px_shishen_line": Template(
        filename="tpl1695691518091.png",
        record_pos=(-0.029, -0.17),
        resolution=(2208, 1242),
    ),
    "action_px_iden_zhandou": Template(
        filename="tpl1695789595400.png",
        record_pos=(-0.162, 0.13),
        resolution=(2208, 1242),
    ),
    # 战斗
    "fight_reward": Template(
        filename="tpl1685414993017.png",
        record_pos=(-0.022, 0.139),
        resolution=(2208, 1242),
    ),
}

dirname = "/images/static/"


def get(name):
    global dirname
    return os.getcwd() + dirname + data[name]


def getTemplate(name):
    filename = get(name)
    if not util.isIOSsys():
        filename = get("A_" + name)
    threshold = dataAttr[name]["threshold"]
    record_pos = dataAttr[name]["threshold"]
    resolution = dataAttr[name]["resolution"]
    # phone screen size
    if not util.isIOSsys():
        resolution = (2340, 1080)
    return Template(
        filename=filename,
        threshold=threshold,
        record_pos=record_pos,
        resolution=resolution,
    )


def getm(name):
    global dirname
    _dirname = dirname
    if "liudao," in name:
        _dirname = "/images/liudao/"
        info = liudao.data[name[7:]]
    else:
        info = dataInfo[name]
    if info.filename.find(_dirname) == -1:
        info.filename = os.getcwd() + _dirname + info.filename
    return info
