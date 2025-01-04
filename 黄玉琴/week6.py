from transformers import BertModel
model = BertModel.from_pretrained('bert-base-uncased')
total_params=sum(p.numel() for p in model.parameters())
print(f'参数量：{total_params}')
