def sd_help():
    help_text = self.get_help_text()
    reply = Reply(help_tex)
    pass
def sd_start():
    if sessionid not in self.draws:
        reply = Reply(
        ReplyType.INFO,
        f"开始画图！请发送图片或文字。该程序是先输入文字描述然后在输入图片进行精修若直接输入图片则使用默认描述。输入{trigger_prefix}sd stop停止画图。",
        )   
    else:
        reply = Reply(ReplyType.INFO, "检测到已经进入画图模式，已重置")
        
    self.draws[sessionid] = StableDiffusion_prompt(bot, sessionid, gpt_set_prompt)
    self.sd_instance[sessionid] = StableDiffusion_draw(sessionid)
 
def sd_stop():
    pass
def sd_config():
    pass
def mj_help():
    pass
def mj_start():
    pass
def mj_stop():
    pass