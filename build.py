import numpy as np

no_malicious = 15013
no_benign = 9779

malicious_tokens = []
malicious_script = []
for i in range(1,no_malicious+1):
    try:
        file_tokenized = '/Volumes/My Passport/Work #2 Dataset/Malicious/tokenized-malicious/'+str(i)+'.txt'
        tmp = []
        with open(file_tokenized) as tokenized:
            for token in tokenized:
                tmp.append(token.split())
            malicious_tokens.append(tmp)

        file_script = '/Volumes/My Passport/Work #2 Dataset/Malicious/malicious-dataset/'+str(i)+'.txt'
        with open(file_script) as script:
            content = script.read()
            malicious_script.append(content)
    except:
        continue

np_malicious_tokens = np.array(malicious_tokens, dtype=object)
np_malicious_script = np.array(malicious_script, dtype=object)

np.save('np_malicious_tokens.npy', np_malicious_tokens)
np.save('np_malicious_script.npy', np_malicious_script)

benign_tokens = []
benign_script = []
for i in range(1,no_benign+1):
    try:
        file_tokenized = '/Volumes/My Passport/Work #2 Dataset/Benign/tokenized-benign/'+str(i)+'.txt'
        tmp = []
        with open(file_tokenized) as tokenized:
            for token in tokenized:
                tmp.append(token.split())
        benign_tokens.append(tmp)

        file_script = '/Volumes/My Passport/Work #2 Dataset/Benign/benign-dataset/'+str(i)+'.txt'
        with open(file_script) as script:
            content = script.read()
            benign_script.append(content)
    except:
        continue



np_benign_tokens = np.array(benign_tokens, dtype=object)
np_benign_script = np.array(benign_script, dtype=object)

np.save('np_benign_tokens.npy', np_benign_tokens)
np.save('np_benign_script.npy', np_benign_script)
    

