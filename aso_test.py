""" Authored by: Neel Kanwal (neel.kanwal0@gmail.com)"""


# Update list of metrics by running inference.py manuscripts 
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)
warnings.simplefilter(action='ignore', category=UserWarning)


import numpy as np
from deepsig import aso

seed = 1234
np.random.seed(seed)

# BLUR VALUES
### 101010
# baseline_mcc = [0.855869827303748,0.5663810381562002,0.9041328746285425,0.9338420877029083, 0.9875916235400559]
# dkl_mcc = [0.9894628550826771, 0.9695106672559797, 0.9847245349518692, 0.8409933056275115, 0.9677098205891904]

# baseline_f1 = [0.924306535025858, 0.704115684093437, 0.9562657695542472, 0.9699054170249355, 0.9943107221006565]
# dkl_f1 = [0.9951648351648352, 0.9860627177700348, 0.9930008748906387, 0.9197960129809921, 0.9852302345786272]

### 888
# baseline_mcc = [0.8482824470654833,0.7568615340901595,0.981808449927857,0.8450872843818916,0.7500871963219756]
# dkl_mcc = [0.9676271102523951, 0.9723413351512266, 0.9847070103442772, 0.971367552010761, 0.9743667561722541]

# baseline_f1 = [0.9312039312039313,0.8654970760233919,0.9916336415675914,0.9301724137931034,0.8595284872298625]
# dkl_f1 = [0.9852045256744997, 0.9873528129088531, 0.9929947460595446, 0.9869109947643979, 0.9882557633753806]

# ### 666
# baseline_mcc = [0.9696776732676289, 0.9594229791232136, 0.965064888827865, 0.9470692851223631, 0.8689876200538034]
# dkl_mcc = [0.9436439419948066, 0.9733496950290529, 0.9809095865812474, 0.9394960939131897, 0.9780981941450634]

# baseline_f1 = [0.9861111111111112, 0.9814254859611231, 0.983989614885331, 0.9749776586237713, 0.9404466501240695]
# dkl_f1 = [0.9742489270386265, 0.9878048780487805, 0.9912587412587412, 0.9713774597495528, 0.9899694723070214]


# # FOLD VALUES

### 666
# baseline_mcc = [0.0, 0.8831826740850759, 0.5290036380274022, 0.0, 0.8831150872608932]
# dkl_mcc = [0.7430670245039158, 0.8376992910052227, 0.7289985785201331, 0.8673301415170699, 0.7415433793210708]

# baseline_f1 = [0.0, 0.8934707903780068, 0.5357873210633947, 0.0, 0.8960573476702509]
# dkl_f1 = [0.7558139534883722, 0.8523489932885907, 0.7401129943502824, 0.8783783783783784, 0.7528735632183908]


### 101010
baseline_mcc = [0.27602698772503387,0.711024998260114,0.8735887496935445,0.6657120373578439,0.15022513082662042]
dkl_mcc = [0.8925447818860257, 0.8516002968953397, 0.8963709078594997, 0.7586326062709635, 0.8367261278513123]


baseline_f1 = [0.31452581032412963,0.7217630853994491,0.8843537414965986,0.6752577319587628,0.23214285714285712]
dkl_f1 = [0.9039145907473309, 0.8648648648648649, 0.9084249084249083, 0.7715133531157271, 0.8478964401294499]



min_eps_mcc = aso(dkl_mcc, baseline_mcc, seed=seed)
min_eps = aso(dkl_f1, baseline_f1, seed=seed)

print(f"Min_eps over mcc = {min_eps_mcc} and over f1 {min_eps}")