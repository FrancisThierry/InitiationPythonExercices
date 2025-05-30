from exercices.design_patterns.ex_cround_funding.mailer import Mailer
from exercices.design_patterns.ex_cround_funding.cagnotte import Cagnotte
from exercices.design_patterns.ex_cround_funding.cagnotte_notifier import CagnotteNotifier
from exercices.design_patterns.ex_cround_funding.cround_funding import CroundFunding
from exercices.design_patterns.ex_cround_funding.small_amount import SmallAmount
from exercices.design_patterns.ex_cround_funding.small_amount_notifier import SmallAmountNotifier
from exercices.design_patterns.ex_cround_funding.user import User
cf = CroundFunding("MyProject", 1000)
user = User("Alice","alice@mns.fr")
mailer = Mailer(user.email)
cagnotte = Cagnotte(cf.goal)
cagnotte_notifier = CagnotteNotifier(cf, user, mailer)
small_amount = SmallAmount(10)
small_amount_notifier = SmallAmountNotifier(small_amount)



cf.add_observer(cagnotte_notifier)
cf.add_observer(small_amount_notifier)
cf.contribute(5)
print(f"Total funds raised: {cf.get_total_funds()}")
cf.contribute(125)
print(f"Total funds raised: {cf.get_total_funds()}")
cf.contribute(125)
print(f"Total funds raised: {cf.get_total_funds()}")
cf.contribute(800)
print(f"Total funds raised: {cf.get_total_funds()}")