# Dummy test file used for messing around with the modules as I was building them out

from preprocessing import UOPreprocessing, ReutersPreprocessing
from dictionary import dictionary
from invertedindex import InvertedIndex
from booleanretrievalmodel import BooleanRetrievalModel
from corpusacess import CorpusAccess
from vectorspacemodel import VectorSpaceModel
from textcategorization import knearestneighbours
import json

if __name__ == "__main__":
    # c = knearestneighbours.KNearestNeighboursClassifier()
    # c.process()
    # proc = ReutersPreprocessing.ReutersPreprocessing()
    # proc.preprocess_collections()

    # uo_dict = dictionary.Dictionary()
    # uo_dict.make_dictionary()

    # inverted_index = InvertedIndex.InvertedIndex()
    # inv_ind = inverted_index.make_inverted_index()

    # b = BooleanRetrievalModel.BooleanRetrievalModel(inv_ind)
    # import pprint
    # # pprint.pprint(b.retrieve('(comput* AND graph*)', 'unaltered'))

    # # corpus_access = CorpusAccess.CorpusAccess()
    # # pprint.pprint(corpus_access.access(['CSI-1', 'CSI-2']))

    import pprint
    v = VectorSpaceModel.VectorSpaceModel()
    v.retrieve('death', 'unaltered')
