from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QDialogButtonBox


class AddArticleDialogLayout(QVBoxLayout):

    def __init__(self):
        super(AddArticleDialogLayout, self).__init__()
        self.product = QLineEdit()
        self.category = QLineEdit()
        self.ok_button = QPushButton('OK')
        self.cancel_button = QPushButton('Cancel')
        product_layout = QHBoxLayout()
        product_layout.addWidget(QLabel('Produkt: '))
        product_layout.addWidget(self.product)
        category_layout = QHBoxLayout()
        category_layout.addWidget(QLabel('Kategoria: '))
        category_layout.addWidget(self.category)
        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonbox = QDialogButtonBox(btn)
        self.addLayout(product_layout)
        self.addLayout(category_layout)
        self.addWidget(self.buttonbox)
