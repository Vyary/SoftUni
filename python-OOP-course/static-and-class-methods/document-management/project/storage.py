from typing import List
from project.document import Document
from project.topic import Topic
from project.category import Category


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = next(
            category for category in self.categories if category.id == category_id
        )
        category.edit(new_name)

    def edit_topic(
        self, topic_id: int, new_topic: str, new_storage_folder: str
    ) -> None:
        topic = next(topic for topic in self.topics if topic.id == topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = next(doc for doc in self.documents if doc.id == document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        category = next(
            category for category in self.categories if category.id == category_id
        )
        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = next(topic for topic in self.topics if topic.id == topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = next(doc for doc in self.documents if doc.id == document_id)
        self.documents.remove(document)

    def get_document(self, document_id: int) -> Document:
        document = next(doc for doc in self.documents if doc.id == document_id)
        return document

    def __repr__(self) -> str:
        return "\n".join(str(document) for document in self.documents)
