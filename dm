# Add Mission Button
icon = qta.icon('mdi6.airplane-clock', color=('#994878', 256))
toolButton = QtWidgets.QToolButton(self)
toolButton.setToolTip("Add Mission")
toolButton.setObjectName("btnAddMission")
toolButton.setIcon(icon)
toolButton.clicked.connect(self.add_mission)  # Connect to the add_mission method
self.button_obj['add_mission'] = toolButton
self.toobar.addWidget(toolButton)

# Delete Mission Button
icon = qta.icon('mdi6.airplane-minus', color=('#DA291C', 256))
toolButton = QtWidgets.QToolButton(self)
toolButton.setToolTip("Remove Mission")
toolButton.setObjectName("btnRemoveMission")
toolButton.setIcon(icon)
toolButton.clicked.connect(self.delete_mission)  # Connect to the delete_mission method
self.button_obj['del_mission'] = toolButton
self.toobar.addWidget(toolButton)

# Define the delete_mission function
def delete_mission(self):
    node = self.ui.treeProject.currentItem()  # Get the currently selected item in the tree
    if isinstance(node, MissionNode):  # Ensure the node is of type MissionNode
        bento_project = node.parent()  # Get the parent project node
        bento_project.study.missions.remove(node.mission)  # Remove the mission from the list
        bento_project.removeChild(node)  # Remove the node from the tree