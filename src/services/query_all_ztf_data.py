'''Query DB for all ZTF data'''

from typing import Sequence, Any
from models.models import Ztf
from . import DATA_PROVIDER


def query_all_ztf_data(start_row: int = 0, end_row: int = -1) -> Any:
    '''Query DB for all ZTF data'''
    all_ztf_data: Sequence[Ztf]
    if end_row == -1:
        all_ztf_data = DATA_PROVIDER.session.query(
            Ztf).order_by(Ztf.obsid).limit(500)
    else:
        all_ztf_data = DATA_PROVIDER.session \
            .query(Ztf).order_by(Ztf.obsid) \
            .offset(start_row) \
            .limit(end_row - start_row)
    return [ztf_row.serialize() for (ztf_row) in all_ztf_data]
