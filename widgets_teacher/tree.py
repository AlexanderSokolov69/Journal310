from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QAbstractItemView, QTreeView, QTreeWidget, QVBoxLayout


class GetNodeDialog(QDialog):
    def __init__(self, parent, startnode, currentnode=None):
        QDialog.__init__(self, parent)

        layout = QVBoxLayout(self)

        self.treeview = QTreeView(self)
        self.treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tree = QTreeWidget(self.treeview)
        self.tree.set_root_node(startnode)
        layout.addWidget(self.treeview)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        layout.addWidget(self.buttons)
        self.resize(800, 600)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.treeview.activated.connect(self.accept)

        if currentnode:
            self.tree.expand_to_node(currentnode)

    def get_node(self):
        return self.tree.get_current_node()

    @staticmethod
    def getNode(parent, startnode, currentnode=None):
        dialog = GetNodeDialog(parent, startnode, currentnode)
        result = dialog.exec_()
        node = dialog.get_node()
        return node, result == QDialog.Accepted