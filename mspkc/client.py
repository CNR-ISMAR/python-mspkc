import logging
from ckanapi import RemoteCKAN
import pandas as pd

logger = logging.getLogger('mspkc')


class Mspkc:
    """Class to retrieve and analyze metadata from a CKAN MSP Knowledge
    Catalogue

    """

    def __init__(self, url=None, apikey=None):
        self.url = url
        self.apikey = apikey
        self.results = None

        self.ckan = RemoteCKAN(self.url,
                               self.apikey)

    def update_result(self, res):
        id = res['id']
        if self.results is None or len(self.results) == 0:
            self.results = [res]
            self.update_df()
            return True
        else:
            for index, item in enumerate(self.results):
                if item['id'] == id:
                    item['id'] = res
                    self.update_df()
                    return True
            self.results.append(res)
            self.update_df()
            return True

    def update_df(self):
        self.df = pd.DataFrame(self.results)

    def load(self, id=None, chunks=100):
        """ """
        start = 0
        count = chunks
        self.results = []
        if id is not None:
            res = self.ckan.action.package_show(id=id)
            self.update_result(res)
            logger.debug("load - package {} loaded".format(id))
            return True

        while len(self.results) < count:
            logger.debug('load - loading chunk {}'.format(count))
            res = self.ckan.action.package_search(include_private=True,
                                                  rows=chunks,
                                                  start=start)
            count = res['count']
            self.results += res['results']
            start += chunks
        self.update_df()
        logger.debug("load - Catalogue loaded")
        return True

    def package_update(self, res):
        self.ckan.action.package_update(**res)
        self.load(id=res['id'])

    # def package_update(self, res):
    #     self.ckan.action.package_update(**res)
    #     self.load(id=res['id'])

    def bulk_replace(self, field, oldval, newval, mode='multi'):
        vals = None

        vals = self.df[field].str.split(',', expand=True)
        condition = vals == oldval
        vals[condition] = newval
        changedrows = vals[condition.any(axis=1)]
        if changedrows.shape[0] > 0:
            newvalues = changedrows.apply(lambda x: x.str.cat(sep=','), axis=1)
            for idx, value in newvalues.iteritems():
                r = self.results[idx]
                print idx, "Update value", r['domain_area'], '-', value
                r['domain_area'] = value
                self.package_update(r)
        else:
            pass
