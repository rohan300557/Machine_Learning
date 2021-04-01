import streamlit as stm
from pickle import load
import pandas as pd
def prdit(data):
    # sc = load(open('pickle/scaler.pkl', 'rb'))
    # modl = load(open("pickle/modl.pkl","rb"))
    stm.write(data)
def main():
    stm.info("educational-num")
    edu_num = stm.slider("",0,10,1)
    stm.info("capital-gain")
    cap_gain = stm.number_input("")
    stm.info("education")
    edu = stm.radio("",("education_5th-6th","education_Preschool","Other"))
    if(edu == "Other"):
        edu_5_6 = 0
        edu_pre = 0
    elif(edu == "education_5th-6th"):
        edu_5_6 = 1
        edu_pre = 0
    elif (edu == "education_Preschool"):
        edu_5_6 = 0
        edu_pre = 1

    stm.info("marital-status")
    mar_status = stm.radio("",("Married-civ-spouse","Married-AF-spouse","Other"))
    if(mar_status == "Other"):
        mar_civ_sp = 0
        mar_af_sp = 0
    elif(mar_status == "Married-civ-spouse"):
        mar_civ_sp = 1
        mar_af_sp = 0
    elif(mar_status == "Married-AF-spouse"):
        mar_civ_sp = 0
        mar_af_sp = 1

    stm.info("occupation")
    occ = stm.radio("",("occupation_Farming-fishing","occupation_Handlers-cleaners",
                        "occupation_Other-service","occupation_Priv-house-serv","Other"))
    if(occ == "occupation_Farming-fishing"):
        occ_far_fish = 1
        occ_han_clean = 0
        occ_oth_sr = 0
        occ_pr_hous_srv = 0
    elif (occ == "occupation_Handlers-cleaners"):
        occ_far_fish = 0
        occ_han_clean = 1
        occ_oth_sr = 0
        occ_pr_hous_srv = 0
    elif (occ == "occupation_Other-service"):
        occ_far_fish = 0
        occ_han_clean = 0
        occ_oth_sr = 1
        occ_pr_hous_srv = 0
    elif (occ == "occupation_Priv-house-serv"):
        occ_far_fish = 0
        occ_han_clean = 0
        occ_oth_sr = 0
        occ_pr_hous_srv = 1
    elif (occ == "Other"):
        occ_far_fish = 0
        occ_han_clean = 0
        occ_oth_sr = 0
        occ_pr_hous_srv = 0

    stm.info("Relationship")
    rel = stm.radio("",("relationship_Other-relative","relationship_Own-child","Other"))
    if(rel == "relationship_Other-relative"):
        rel_oth_rel = 1
        rel_own_chl = 0
    elif (rel == "relationship_Other-relative"):
        rel_oth_rel = 0
        rel_own_chl = 1
    elif(rel == "Other"):
        rel_oth_rel = 0
        rel_own_chl = 0

    stm.info("Native")
    nat = stm.radio("",("native-country_Columbia","native-country_Dominican-Republic",
                            "native-country_Guatemala","native-country_Laos",
                            "native-country_Mexico","native-country_Nicaragua",
                            "native-country_South","native-country_Vietnam","Other"))
    if(nat == "native-country_Columbia"):
        nat_con_col = 1
        nat_con_dom = 0
        nat_con_gat = 0
        nat_con_laos = 0
        nat_con_m = 0
        nat_col_nicar = 0
        nat_col_south = 0
        nat_col_vitn = 0
    elif(nat == "native-country_Dominican-Republic"):
        nat_con_col = 0
        nat_con_dom = 1
        nat_con_gat = 0
        nat_con_laos = 0
        nat_con_m = 0
        nat_col_nicar = 0
        nat_col_south = 0
        nat_col_vitn = 0
    elif (nat == "native-country_Guatemala"):
        nat_con_col = 0
        nat_con_dom = 0
        nat_con_gat = 1
        nat_con_laos = 0
        nat_con_m = 0
        nat_col_nicar = 0
        nat_col_south = 0
        nat_col_vitn = 0
    elif (nat == "native-country_Laos"):
        nat_con_col = 0
        nat_con_dom = 0
        nat_con_gat = 0
        nat_con_laos = 1
        nat_con_m = 0
        nat_col_nicar = 0
        nat_col_south = 0
        nat_col_vitn = 0
    elif (nat == "native-country_Mexico"):
        nat_con_col = 0
        nat_con_dom = 0
        nat_con_gat = 0
        nat_con_laos = 0
        nat_con_m = 1
        nat_col_nicar = 0
        nat_col_south = 0
        nat_col_vitn = 0
    elif (nat == "native-country_Nicaragua"):
        nat_con_col = 0
        nat_con_dom = 0
        nat_con_gat = 0
        nat_con_laos = 0
        nat_con_m = 0
        nat_col_nicar = 1
        nat_col_south = 0
        nat_col_vitn = 0
    elif (nat == "native-country_South"):
        nat_con_col = 0
        nat_con_dom = 0
        nat_con_gat = 0
        nat_con_laos = 0
        nat_con_m = 0
        nat_col_nicar = 0
        nat_col_south = 1
        nat_col_vitn = 0
    elif (nat == "native-country_South"):
        nat_con_col = 0
        nat_con_dom = 0
        nat_con_gat = 0
        nat_con_laos = 0
        nat_con_m = 0
        nat_col_nicar = 0
        nat_col_south = 0
        nat_col_vitn = 1
    elif (nat == "Other"):
        nat_con_col = 0
        nat_con_dom = 0
        nat_con_gat = 0
        nat_con_laos = 0
        nat_con_m = 0
        nat_col_nicar = 0
        nat_col_south = 0
        nat_col_vitn = 0
    data = [edu_num,cap_gain,edu_5_6,edu_pre,mar_af_sp,mar_civ_sp,occ_far_fish,occ_han_clean,
            occ_oth_sr,occ_pr_hous_srv,rel_oth_rel,rel_own_chl,nat_con_col,nat_con_dom,nat_con_gat,
            nat_con_laos,nat_con_m,nat_col_nicar,nat_col_south,nat_col_vitn]
    pr = prdit(data)
    stm.write(pr)
    stm.write(data )

    da = [4,0.04000000000000001,
0,
1,
1,
0,
0,
0,
0,
1,
1,
0,
1,
0,
0,
0,
0,
0,
0,
0]
df1 = pd.DataFrame([da])
print(df1)

if __name__ == '__main__':
    main()
