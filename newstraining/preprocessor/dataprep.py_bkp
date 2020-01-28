import pandas as pd
import numpy as np

dataset = pd.read_csv('D:\\ml and dl\\keras\\dataset\\dataset_1.csv')
print(dataset.columns)

newsDataset = dataset[['fact_rating_phase1','article_title_phase1','original_article_text_phase2','author_phase2']]
newsDataset = newsDataset.rename(columns={'fact_rating_phase1':'fact_check','article_title_phase1':'title',
                            'original_article_text_phase2':'content','author_phase2':'author'})
print(newsDataset.columns)
print(newsDataset['fact_check'].value_counts())
newsDataset_false = newsDataset.loc[(newsDataset['fact_check']=='false')]
newsDataset_true =  newsDataset.loc[(newsDataset['fact_check']=='true')]
print(newsDataset_false['fact_check'].value_counts())
print(newsDataset_false.shape)

indices_false = np.random.randint(0, 7972, size=(20))
indices_true = np.random.randint(0, 1619, size=(60))

false_dataset = newsDataset_false.iloc[indices_false]
true_dataset = newsDataset_true.iloc[indices_true]

dataset = false_dataset.append(true_dataset)
dataset.to_csv ('D:\\ml and dl\\keras\\dataset\\dataset_final.csv', index = None, header=True)

print('hello')