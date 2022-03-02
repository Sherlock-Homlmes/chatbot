


def xuly(message):
  message = message.lower()
  print(message)

  if "chào" in message:
    return "xin chào bạn"
  elif "htu" in message:
    return "huyền đang làm gì vậy"
  elif "tên gì" in message:
    return "mình tên là mie"    
  elif "wakeup" in message:
    return "dậy đi Lôli"
  elif "cheng" in message:
    return "Xin chào cheng"
  elif "bánh" in message:
    return "Xin chào Bánh"    
  elif "loli" in message:
    return "Xin chào Lô li"    
  elif "ngủ ngon" in message:
    return "chúc bạn ngủ ngon"           
  elif "tạm biệt" in message:
    return "Tạm biệt bạn nha"
  elif "láo" in message:
    return "mày mới láo"

  else:
    return "xin lỗi bạn mình chưa trả lời được câu này"