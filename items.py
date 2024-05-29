class Items():
  def __init__(self, name: str, description: str, progress: int ):
    self.name = name
    self.description = description
    self.progress = progress 

  pass

autopsy = Items(name = "Improved Autopsy",
               description = "The greatest minds here came up with this",
               progress = 0)
bullet_casing = Items(name = "5.11 Bullet Casing",
   description = "The 5.11 usually belongs to SE brand guns",
   progress = 0)
lucas_gun = Items(name = "SER Revolver",
   description = "These are usually assigned to military personnel",
   progress = 0)
vixen_gun = Items(name = "SE Semi Automatic",
   description = "A weapon commonly associated with people down on their luck",
   progress = 0)
safe_keycard = Items(name = "Grimy Piece of Paper",
   description = "A scrap of paper with the numbers 1294. It's covered with red stains",
   progress = 0)
