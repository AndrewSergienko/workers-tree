from mptt.querysets import TreeQuerySet

from workers.models import Worker


def get_worker_by_id(pk) -> Worker:
    return Worker.objects.get(id=pk)


def get_root_worker() -> Worker:
    return Worker.objects.get(position="1")


def get_worker_children(worker: Worker) -> TreeQuerySet[Worker]:
    return worker.get_children()
