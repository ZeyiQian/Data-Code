
****修改后matrix

***随机化p值
*matrix t = J(1, 2, .)	
reg balance_sept30 fingerprint i.focode##i.offer_week, cluster(bfirm_club_id)
matrix t = (abs(e(b)[1,1]/sqrt(e(V)[1,1])), 1)

*matrix t = J(999, 2, .)
forvalues i = 1/999 {
   qui  gen rand = runiform()
   qui egen total = total(rand), by(bfirm_club_id)
   qui ereplace rand = total(rand), by(bfirm_club_id)
   qui egen rank = group(rand)
    qui gen fake_treat = (rank <= 61)
    qui reg balance_sept30  fake_treat fingerprint i.focode##i.offer_week, cluster(bfirm_club_id)
    drop rand total rank fake_treat
	matrix t = (t\ abs(e(b)[1,1]/sqrt(e(V)[1,1])),0)
}

clear
svmat t
gsort-t1
gen p= _n/_N
***找出比原来的t大的假t的个数除以1000就是随机下的p值
