from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def get(self):
        ...

    @abstractmethod
    async def get_list(self):
        ...

    @abstractmethod
    async def save(self):
        ...

    @abstractmethod
    async def delete(self):
        ...


class Repository(AbstractRepository):
    async def get(self):
        raise NotImplementedError()

    async def get_list(self):
        raise NotImplementedError()

    async def save(self):
        raise NotImplementedError()

    async def delete(self):
        raise NotImplementedError()


class RepositoryMemory(AbstractRepository):
    """
    Repository for development, stored in RAM
    """
    async def get(self):
        raise NotImplementedError()

    async def get_list(self):
        raise NotImplementedError()

    async def save(self):
        raise NotImplementedError()

    async def delete(self):
        raise NotImplementedError()