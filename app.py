import pandas as pd
# import numpy as np
import streamlit as st
import altair as alt

st.set_page_config(
    page_title="Disparitas Korban Tindakan Kriminal di Los Angeles",
    page_icon=":chart:",
    layout="wide",
    initial_sidebar_state="expanded",                                      
)                    
  
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>Disparitas Korban Tindakan Kriminal di Los Angeles</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>By: Alfarabi Muzli</p>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(['🏚️ Narasi', '🗺️ By Area', 'ℹ️ By Status', '🧑‍🤝‍🧑 By Descent', '👆 About Me'])

with tab1:
    '''
        Amerika Serikat, atau USA, merupakan salah satu negara adidaya yang memiliki pengaruh besar dalam politik internasional,
        memengaruhi aspek kehidupan global seperti politik, ekonomi, dan keamanan. Dalam aspek ekonomi, Amerika Serikat
        termasuk negara dengan ekonomi yang kuat, berada di peringkat 25 dunia setelah Uni Emirat Arab yang berada di peringkat 24 (sc: [_2023 Index of Economic Freedom_](https://www.heritage.org/index/country/unitedstates)).
        Namun, bagaimana dengan keamanan? Apakah juga termasuk negara dengan tingkat keamanan tinggi?
        Jika kita melihat berita yang ada, Amerika Serikat dalam 25 tahun terakhir telah berusaha menekan tingkat kejahatan dengan cukup sukses,
        mencatat angka sebesar **47.70**, yang mana relatif rendah jika dibandingkan dengan negara-negara seperti Venezuela (83.76) dan Papua Nugini (80.79), yang memiliki tingkat kejahatan tertinggi.
    '''
    '''
    Dalam beberapa waktu terakhir, tingkat kriminalitas di Los Angeles telah meningkat, sehingga Konsulat Jenderal Republik Indonesia (KJRI) memberikan imbauan kepada WNI untuk meningkatkan kewaspadaan saat berada di kota tersebut. Tingkat kriminalitas yang meningkat telah mengakibatkan sejumlah korban mengalami luka serius dan bahkan masuk unit perawatan intensif (ICU) di pusat kota Los Angeles.
    
    '''

    df1 = pd.read_csv('dataset/Crime_Dataset_Sol-2(0,Mode,Mode).csv')

    st.header('Jumlah Korban')

    penjelasan, chart = st.columns([2, 1])

    with penjelasan:
        '''
        Data dari _Los Angeles Police Department_ menunjukkan bahwa dari tahun 2020 hingga 2023, laki-laki (ditandai warna merah) mendominasi sebagai korban tindak kriminalitas,
        dengan proporsi sebesar 54%, sedangkan wanita (ditandai warna biru) mencapai 37%. Berdasarkan data statistik dari _Bireau of Justice Statistic_, laki-laki lebih sering menjadi korban kekerasan daripada wanita di Amerika Serikat, yang mana menjustifikasi data korban kriminal di Los Angeles (sc. [Sex Differences in Crime](https://en.wikipedia.org/wiki/Sex_differences_in_crime)).
        Adapun mengenai pelaku tindak kriminal, mayoritas adalah laki-laki. Pada tahun 2001, misalnya, sekitar 5 juta laki-laki dipenjara, di mana 80% dari mereka dihukum karena kekerasan dan 69% karena pencurian.
        Hal ini mencerminkan pola umum di mana laki-laki memiliki kecenderungan yang lebih tinggi untuk terlibat dalam kekerasan dan kejahatan lainnya daripada wanita.
        Faktor-faktor yang mendasari kesenjangan gender dalam tindak kriminalitas, baik sebagai korban maupun pelaku, melibatkan dinamika sosial, ekonomi, dan budaya yang kompleks.
        '''
        '''
        Namun, tidak semua data korban kriminalitas mencatat jenis kelamin, seperti yang ditunjukkan dalam bagan di samping. Hal ini bisa disebabkan oleh beberapa alasan:
        1. Jenis Kelamin memang tidak diketahui karena adanya faktor eksternal misalnya korban tidak diketahui siapa,
        2. Jenis kelamin sengaja tidak dipublikasikan untuk melindungi privasi keluarga korban atau korban itu sendiri, dan
        3. Ada kemungkinan korban merupakan Non-Binary, yang cukup umum di Amerika Serikat.
        
        Kemungkinan yang paling masuk akal adalah nomor 3, karena penting untuk mencatat jenis kelamin korban sebagai langkah antisipasi bagi masyarakat. Dalam tulisan ini, hanya menggunakan dua jenis kelamin,
        yaitu M untuk laki-laki dan F untuk perempuan. Untuk kasus di mana jenis kelamin tidak diketahui, menggunakan kategori X atau "Unknown".
        '''
        
    with chart:
        victim_sex_counts = df1['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
    
    victim_sex_counts = df1['Vict Sex'].value_counts().reset_index()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Jumlah Korban Laki-Laki", value=victim_sex_counts['count'][0])
    
    with col2:
        st.metric("Jumlah Korban Perempuan", value=victim_sex_counts['count'][1])

    with col3:
        st.metric("Jumlah Korban Jenis Kelamin Tidak Diketahui", value=victim_sex_counts['count'][2])
        
        
    st.subheader('Korban berdasarkan umur')

    age_ranges = [(0, 0), (1, 18), (19, 30), (31, 40), (41, 50), (51, 100)]

    def categorize_age(age):
        for i, (start, end) in enumerate(age_ranges):
            if start <= age <= end:
                if start == end:
                    return str(start)
                else:
                    return f'{start}-{end}'

    df1['Age Range'] = df1['Vict Age'].apply(categorize_age)

    grouped_data = df1.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
    melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')

    chart2, penjelasan2 = st.columns([1.5, 1.5])

    with chart2:
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)

    with penjelasan2:
        '''
        Dari bagan di samping, terlihat persebaran korban berdasarkan usia. Ternyata, rentang usia 19-30 tahun merupakan rentang usia dengan jumlah korban terbanyak,
        mencapai sekitar 180.000 kasus. Lebih jauh, data juga menunjukkan bahwa jumlah korban perempuan lebih tinggi daripada jumlah korban laki-laki,
        dengan perempuan mencatat sekitar 96.283 kasus dan laki-laki sekitar 84.523 kasus dalam rentang usia tersebut,
        sehingga menjadikan rentang usia korban perempuan ini sebagai yang terbanyak tercatat dalam data.
        '''
        '''
        Hal ini menunjukkan bahwa korban berada pada masa transisi dari remaja menuju dunia dewasa banyak dijadikan korban kejahatan.
        Hal ini terjadi karena pada rentang usia tersebut, banyak individu sedang dalam fase kehidupan yang penuh tantangan,
        seperti memulai karier, menetapkan hubungan interpersonal yang lebih serius, dan mungkin kurang waspada terhadap risiko kejahatan.        
        '''
        '''
        Jika diperhatikan lebih lanjut, dalam bagan tersebut terdapat definisi untuk rentang usia 0, yang menunjukkan bahwa usia korban tidak
        diketahui karena beberapa faktor internal. Dalam konteks ini, rentang usia tersebut dapat dikategorikan sebagai "Unknown".
        '''
    
    st.subheader('Jenis Kejahatan Berdasarkan Jenis Kelamin')
    sex = st.selectbox("Jenis Kelamin", ['Male', 'Female'])
    colm1, colm2 = st.columns(2)
    if sex == 'Male':
        with colm1:
            dfM = df1[df1['Vict Sex'] == 'M']
            crime_desc_M = dfM['Crm Cd Desc'].value_counts()
            top_crimes_M = crime_desc_M.head(5).reset_index()
            
            bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
            x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                    sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
            y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
            ).properties(
            title='Distribution of Crime Description based on Male Victims',
            width=600,
            height=400
            ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
            st.altair_chart(bar_chart)
            
        with colm2:
            top_crimes_M = crime_desc_M.reset_index()
            top_5 = crime_desc_M.head(1).reset_index()
            last_value = top_crimes_M.iloc[-1]
            least_value = last_value['Crm Cd Desc']
            least_count = last_value['count']
            # st.write(top_5)
            st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
            st.metric("Jumlah Kasus", value=top_5['count'][0])
            st.metric("Tindakan kriminal Terendah", value=least_value)
            st.metric("Jumlah Kasus", value=least_count)
        
        # '''
        # Berdasarkan data yang terdapat pada bagan dan tabel di atas, dapat disimpulkan bahwa tindak kriminal yang paling banyak terjadi pada laki-laki adalah pencurian kendaraan,
        # yang mencapai 93 ribu kasus. Hal ini diikuti oleh serangan sederhana, serangan mematikan dengan senjata, perampokan dari kendaraan, dan pencurian dari motor.
        # Hal ini disebabkan oleh Laki-laki cenderung lebih terlibat dalam aktivitas yang melibatkan kendaraan, seperti mengemudi atau memiliki kendaraan bermotor. Karena keterlibatan ini, mereka mungkin lebih rentan menjadi pelaku atau korban pencurian kendaraan.
        # Apalagi banyak kekerasan yang berhubungan dengan keadaan ekonomi, kendaraan itu sendiri memiliki nilai ekonomi yang cukup tinggi sehingga menjadi sasaran untuk pelaku pencurian.
        # '''

    if sex == 'Female':
        with colm1:
            dfW = df1[df1['Vict Sex'] == 'F']
            crime_desc_W = dfW['Crm Cd Desc'].value_counts()
            top_crimes_W = crime_desc_W.head(5).reset_index()
            
            bar_chart = alt.Chart(top_crimes_W).mark_bar().encode(
            x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                    sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
            y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
            ).properties(
            title='Distribution of Crime Description based on Female Victims',
            width=600,
            height=400
            ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
            st.altair_chart(bar_chart)
            
        with colm2:
            top_5 = crime_desc_W.head(1).reset_index()
            top_crimes_W = crime_desc_W.reset_index()
            last_value = top_crimes_W.iloc[-1]
            least_value = last_value['Crm Cd Desc']
            least_count = last_value['count']
            # st.write(top_5['Crm Cd Desc'])
            st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
            st.metric("Jumlah Kasus", value=top_5['count'][0])
            st.metric("Tindakan kriminal Terendah", value=least_value)
            st.metric("Jumlah Kasus", value=least_count)
        
        # '''
        # Berdasarkan bagan dan tabel yang disajikan, terlihat bahwa tindak kriminal yang paling sering terjadi pada perempuan adalah kekerasan oleh pasangan, dengan jumlah kasus mencapai 33 ribu.
        # Ini diikuti oleh penyerangan sederhana, pencurian identitas, perampokan dari kendaraan, dan pencurian.
        # Salah satu alasannya adalah pola yang meluas maksudnya adalah pola ini dapat disebabkan oleh ketidaksetaraan gender, kontrol kekuasaan, dan faktor-faktor sosial dan psikologis lainnya yang memengaruhi hubungan interpersonal.
        # '''
    
    '''
    Pioritas tindak kriminal yang dominan pada masing-masing gender. 
    Bagi laki-laki, pencurian kendaraan menjadi kejahatan kriminal terbanyak, Hal ini bisa terjadi karena mereka seringkali melakukan perjalanan malam hari (sc. [AVIVA Car Insurance](https://www.aviva.co.uk/aviva-edit/your-things-articles/keyless-car-thefts)).
    Sedangkan perempuan didominasi dalam tindak kriminal kekerasan oleh pasangan. Hal ini bisa terjadi karena beberapa faktor seperti faktor psikologi, pelanggaran antar pasangan, cari perhatian, dan menjaga _image_ (sc. [National Library of Medicine](10.1891/1946-6560.5.4.359)).
    '''
    
    st.header('Kesimpulan')
    '''
    Kesimpulan dari data yang disajikan adalah bahwa tindak kriminalitas di Amerika Serikat, khususnya di Los Angeles memiliki dampak yang signifikan, dengan laki-laki dominan sebagai korban, sementara perempuan lebih rentan terhadap kekerasan oleh pasangan. Rentang usia 19-30 tahun merupakan rentang usia dengan jumlah korban terbanyak,
    menunjukkan bahwa masa transisi dari remaja menuju dewasa adalah periode yang rentan terhadap kejahatan. Meskipun ada kesamaan dalam beberapa jenis kejahatan yang dialami baik oleh laki-laki maupun perempuan, terdapat perbedaan dalam prioritas tindak kriminal yang dominan pada masing-masing gender.
    '''
    '''
    Berbekal data kriminalitas di Los Angeles, bisa dimanfaatkan sebagai penghindaran tindak kriminalitas dimasa depan dengan cara:
    1. Dengan meningkatkan akses terhadap pendidikan, pekerjaan, dan kesempatan ekonomi,
    2. Memberikan pelatihan dan pendidikan terhadap individu yang membutuhkan, dan
    3. Meningkatkan layanan konseling, bantuan hukum
    '''
    '''
    Juga memberikan himbauan kepada masyarakat agar selalu berhati-hati agar tidak berpergian atau melakukan perjalanan pada malam hari jika tidak _urgent_, jika terjadi _domistic violence_ terhadap pasangan lebih baik untuk 
    melapor pihak berwenang atau hubungi konseling.
    '''

    '''
    Daftar Pustaka
    1. [LAPD Crime Data 2020 - 2023](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data)
    2. [_2023 Index of Economic Freedom_](https://www.heritage.org/index/country/unitedstates)
    3. [Sex Differences in Crime](https://en.wikipedia.org/wiki/Sex_differences_in_crime)
    4. [AVIVA Car Insurance](https://www.aviva.co.uk/aviva-edit/your-things-articles/keyless-car-thefts)
    5. [National Library of Medicine](10.1891/1946-6560.5.4.359)
    '''

with tab2:
    st.header('Berdasarkan Area')
    unique_area = df1['AREA NAME'].unique()
    
    area = st.selectbox("Area", ['Wilshire', 'Central', 'Southwest', 'Van Nuys', 'Hollywood',
            'Southeast', 'Newton', 'Mission', 'Rampart', 'Hollenbeck', 
            'West Valley', 'West LA', 'Olympic', 'Topanga', 'Northeast',
            '77th Street', 'Pacific', 'N Hollywood', 'Harbor', 'Foothill', 'Devonshire'])
    
    if area=='Wilshire':
        dfwil = df1[df1['AREA NAME']=='Wilshire']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfwil['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfwil.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Wilshire Male', 'Wilshire Female'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Wilshire Male':
            with col1:
                dfM = dfwil[dfwil['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Wilshire Female':
            with col1:
                dfM = dfwil[dfwil['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
        
    
    if area=='Central':
        dfcen = df1[df1['AREA NAME']=='Central']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfcen['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfcen.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Central Males', 'Central Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Central Males':
            with col1:
                dfM = dfcen[dfcen['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Central Females':
            with col1:
                dfM = dfcen[dfcen['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Southwest':
        dfsouth = df1[df1['AREA NAME']=='Southwest']
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfsouth['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfsouth.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Southwest Males', 'Southwest Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Southwest Males':
            with col1:
                dfM = dfsouth[dfsouth['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Southwest Females':
            with col1:
                dfM = dfsouth[dfsouth['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
                
    if area=='Van Nuys':
        dfvan = df1[df1['AREA NAME']=='Van Nuys']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfvan['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfvan.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Van Nuys Males', 'Van Nuys Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Van Nuys Males':
            with col1:
                dfM = dfvan[dfvan['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Van Nuys Females':
            with col1:
                dfM = dfvan[dfvan['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Hollywood':
        dfhol = df1[df1['AREA NAME']=='Hollywood']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfhol['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfhol.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Hollywood Males', 'Hollywood Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Hollywood Males':
            with col1:
                dfM = dfhol[dfhol['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Hollywood Females':
            with col1:
                dfM = dfhol[dfhol['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Southeast':
        dfsouthe = df1[df1['AREA NAME']=='Southeast']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfsouthe['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfsouthe.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Southeast Males', 'Southeast Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Southeast Males':
            with col1:
                dfM = dfsouthe[dfsouthe['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Southeast Females':
            with col1:
                dfM = dfsouthe[dfsouthe['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Newton':
        dfnewt = df1[df1['AREA NAME']=='Newton']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfnewt['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfnewt.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Newton Males', 'Newton Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Newton Males':
            with col1:
                dfM = dfnewt[dfnewt['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Newton Females':
            with col1:
                dfM = dfnewt[dfnewt['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Mission':
        dfmiss = df1[df1['AREA NAME']=='Mission']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfmiss['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfmiss.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Mission Males', 'Mission Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Mission Males':
            with col1:
                dfM = dfmiss[dfmiss['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Mission Females':
            with col1:
                dfM = dfmiss[dfmiss['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Rampart':
        dframp = df1[df1['AREA NAME']=='Rampart']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dframp['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dframp.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Rampart Males', 'Rampart Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Rampart Males':
            with col1:
                dfM = dframp[dframp['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Rampart Females':
            with col1:
                dfM = dframp[dframp['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Hollenbeck':
        dfbeck = df1[df1['AREA NAME']=='Hollenbeck']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfbeck['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfbeck.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Hollenbeck Males', 'Hollenbeck Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Hollenbeck Males':
            with col1:
                dfM = dfbeck[dfbeck['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Hollenbeck Females':
            with col1:
                dfM = dfbeck[dfbeck['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='West Valley':
        dfvall = df1[df1['AREA NAME']=='West Valley']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfvall['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfvall.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['West Valley Males', 'West Valley Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'West Valley Males':
            with col1:
                dfM = dfvall[dfvall['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'West Valley Females':
            with col1:
                dfM = dfvall[dfvall['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if area=='West LA':
        dfLA = df1[df1['AREA NAME']=='WestLA']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfLA['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfLA.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['West LA Males', 'West LA Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'West LA Males':
            with col1:
                dfM = dfLA[dfLA['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'West LA Females':
            with col1:
                dfM = dfLA[dfLA['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Olympic':
        dfmpi = df1[df1['AREA NAME']=='Olympic']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfmpi['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfmpi.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Olympic Males', 'Olympic Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Olympic Males':
            with col1:
                dfM = dfmpi[dfmpi['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Olympic Females':
            with col1:
                dfM = dfmpi[dfmpi['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Topanga':
        dftop = df1[df1['AREA NAME']=='Topanga']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dftop['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dftop.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Topanga Males', 'Topanga Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Topanga Males':
            with col1:
                dfM = dftop[dftop['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Topanga Females':
            with col1:
                dfM = dftop[dftop['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Northeast':
        dfnorth = df1[df1['AREA NAME']=='Northeast']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfnorth['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfnorth.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Northeast Males', 'Northeast Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Northeast Males':
            with col1:
                dfM = dfnorth[dfnorth['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Northeast Females':
            with col1:
                dfM = dfnorth[dfnorth['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if area=='77th Street':
        df77 = df1[df1['AREA NAME']=='77th Street']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = df77['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = df77.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['77th Street Males', '77th Street Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == '77th Street Males':
            with col1:
                dfM = df77[df77['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == '77th Street Females':
            with col1:
                dfM = df77[df77['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if area=='Pacific':
        dfpac = df1[df1['AREA NAME']=='Pacific']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfpac['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfpac.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Pacific Males', 'Pacific Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Pacific Males':
            with col1:
                dfM = dfpac[dfpac['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Pacific Females':
            with col1:
                dfM = dfpac[dfpac['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if area=='N Hollywood':
        dfnhol = df1[df1['AREA NAME']=='N Hollywood']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfnhol['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfnhol.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['N Hollywood Males', 'N Hollywood Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'N Hollywood Males':
            with col1:
                dfM = dfnhol[dfnhol['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'N Hollywood Females':
            with col1:
                dfM = dfnhol[dfnhol['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if area=='Harbor':
        dfhar = df1[df1['AREA NAME']=='Harbor']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfhar['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfhar.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Harbor Males', 'Harbor Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Harbor Males':
            with col1:
                dfM = dfhar[dfhar['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Harbor Females':
            with col1:
                dfM = dfhar[dfhar['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if area=='Foothill':
        dfoot = df1[df1['AREA NAME']=='Foothill']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfoot['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfoot.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Foothill Males', 'Foothill Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Foothill Males':
            with col1:
                dfM = dfoot[dfoot['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Foothill Females':
            with col1:
                dfM = dfoot[dfoot['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if area=='Devonshire':
        dfon = df1[df1['AREA NAME']=='Devonshire']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfon['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfon.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Devonshire Males', 'Devonshire Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Devonshire Males':
            with col1:
                dfM = dfon[dfon['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Devonshire Females':
            with col1:
                dfM = dfon[dfon['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
                

with tab3:
    '''
    Status sendiri merupakan status dari kasusnya, apakah masih berlanjut investigasi atau sudah dalam penyelesaian.
    '''
    '''
    Status pada data ini terbagi menjadi beberapa kategori yaitu:
    1. IC = Masih dalam Penyelidikan
    2. AA = Adult Arrest
    3. JA = Juvenile Arrest
    4. JO = Juvenile Other
    5. AO = Adult Other
    6. CC = Unknown
    '''

    status = st.selectbox("Status", ['IC Investigation Continue', 'AA Adult Arrest', 'JA Juvenile Arrest', 'JO Juvenile Other', 'AO Adult Other', 'CC UNK'])
    
    if status == 'IC Investigation Continue':
        dfic = df1[df1['Status']=='IC']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfic['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfic.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['IC Males', 'IC Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'IC Males':
            with col1:
                dfM = dfic[dfic['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'IC Females':
            with col1:
                dfM = dfic[dfic['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if status == 'AA Adult Arrest':
        dfaa = df1[df1['Status']=='AA']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfaa['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfaa.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['AA Males', 'AA Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'AA Males':
            with col1:
                dfM = dfaa[dfaa['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'AA Females':
            with col1:
                dfM = dfaa[dfaa['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if status == 'JA Juvenile Arrest':
        dfja = df1[df1['Status']=='JA']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfja['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfja.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['JA Males', 'JA Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'JA Males':
            with col1:
                dfM = dfja[dfja['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'JA Females':
            with col1:
                dfM = dfja[dfja['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if status == 'AO Adult Other':
        dfao = df1[df1['Status']=='AO']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfao['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfao.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['AO Males', 'AO Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'AO Males':
            with col1:
                dfM = dfao[dfao['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'AO Females':
            with col1:
                dfM = dfao[dfao['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if status == 'JO Juvenile Other':
        dfjo = df1[df1['Status']=='JO']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfjo['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfjo.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['JO Males', 'JO Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'JO Males':
            with col1:
                dfM = dfjo[dfjo['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'JO Females':
            with col1:
                dfM = dfjo[dfjo['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        
    if status == 'CC UNK':
        dfcc = df1[df1['Status']=='CC']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfcc['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfcc.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['CC Males', 'CC Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'CC Males':
            with col1:
                dfM = dfcc[dfcc['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'CC Females':
            with col1:
                dfM = dfcc[dfcc['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    

with tab4:
    '''
    Bukan ingin mengarah ke SARA, tetapi seperti yang kita ketahui bahwa Amerika Serikat hidup dalam basis stereotipe-stereotipe yang ada. Misalnya seperti masyarakat keturunan
    kulit putih atau Caucasian yang menjadi superior, keturunan kulit hitam atau African-American yang sering diasosiasikan dengan pelaku kriminal, dan Masyarakat keturunan Hispanic atau latin
    yang sering disebut sebagai tenaga kerja. Berdasarkan data polisi yang dikumpulkan oleh Pusat Studi Kebencian dan Ekstremisme di _California State University_ di San Bernandino,
    menyebutkan bahwa sepanjang tahun 2022 kejahatan _hate crime_ atau kejahatan bermotif kebencian  meningkat sebesar 5% dari tahun sebelumnya yaitu sebesar 30%.
    Biro Penyidik FBI menyatakan bahwa motif dari kejahatan kebencian berdasarkan dari bias pelaku terhadap SARA. Kejahatan kebencian sendiri semenjak terjadinya wabah corona-19, meningkat setiap tahunnya,
    apalagi ketika peristiwa tewasnya seorang warga Amerika keturunan African-American, Gorge Floyd, di tangan polisi pada tahun 2020 silam
    (sc [VoA Indonesia](https://www.voaindonesia.com/a/kejahatan-bermotif-kebencian-di-as-meningkat-sepanjang-2022/6714277.html)).
    '''
    '''
    Berdasarkan paparan tersebut, dilakukan analisis terhadap persebaran korban berdasarkan keturunan yang banyak populasinya di Amerika Serikat yaitu '**Caucasian**', '**African-American**', dan '**Hispanic**'.
    '''
    descent = st.selectbox("Keturunan", ['Caucasian', 'African-American', 'Hispanic'])

    if descent == 'Caucasian':
        dfW = df1[df1['Vict Descent']=='W']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfW['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfW.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Caucasian Males', 'Caucasian Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Caucasian Males':
            with col1:
                dfM = dfW[dfW['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Caucasian Females':
            with col1:
                dfM = dfW[dfW['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if descent == 'African-American':
        dfB = df1[df1['Vict Descent']=='B']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfB['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfB.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['African-American Males', 'African-American Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'African-American Males':
            with col1:
                dfM = dfB[dfB['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'African-American Females':
            with col1:
                dfM = dfB[dfB['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
    
    if descent == 'Hispanic':
        dfH = df1[df1['Vict Descent']=='H']
        
        st.subheader('Berdasarkan Jenis Kelamin')
        
        victim_sex_counts = dfH['Vict Sex'].value_counts().reset_index()
        victim_sex_counts.columns = ['Vict Sex', 'Count']
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        pie_chart = alt.Chart(victim_sex_counts).mark_arc().encode(
            theta='Count',
            color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold', orient='bottom'))
        ).properties(
            width=500,
            height=400   
        ).properties(
            title=alt.Title(text='Victim Sex Distribution', align='center')
        ).configure(background='rgba(0,0,0,0)').interactive()
        st.altair_chart(pie_chart)
        
        st.subheader('Berdasarkan Rentang Umur')
        
        grouped_data = dfH.groupby(['Age Range', 'Vict Sex']).size().unstack(fill_value=0).reset_index()
        melted_data = pd.melt(grouped_data, id_vars=['Age Range'], var_name='Vict Sex', value_name='Number of Victims')
        
        custom_color_scale = alt.Scale(domain=['M', 'F', 'X'], range=['#D81B60', '#1E88E5', '#FFC107'])
        
        bar_chart = alt.Chart(melted_data).mark_bar().encode(
        x=alt.X('Age Range', axis=alt.Axis(labelFontWeight='bold')),
        y=alt.Y('Number of Victims', axis=alt.Axis(labelFontWeight='bold')),
        color=alt.Color('Vict Sex', scale=custom_color_scale, legend=alt.Legend(labelFontWeight='bold')),
        tooltip=['Age Range', 'Vict Sex', 'Number of Victims']
        ).properties(
        title='Distribution of Victims by Age Range and Victim Sex',
        width=600,
        height=400
        ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
        st.altair_chart(bar_chart)
        
        st.subheader('Berdasarkan Jenis Kejahatan')
        
        sex_s = st.selectbox("Jenis Kelamin", ['Hispanic Males', 'Hispanic Females'])
        col1, col2 = st.columns(2)
        
        if sex_s == 'Hispanic Males':
            with col1:
                dfM = dfH[dfH['Vict Sex'] == 'M']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Male Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])
        if sex_s == 'Hispanic Females':
            with col1:
                dfM = dfH[dfH['Vict Sex'] == 'F']
                crime_desc_M = dfM['Crm Cd Desc'].value_counts()
                top_crimes_M = crime_desc_M.head(5).reset_index()
                
                bar_chart = alt.Chart(top_crimes_M).mark_bar().encode(
                x=alt.X('Crm Cd Desc', axis=alt.Axis(labelAngle=45, labelFontWeight='bold'),
                        sort=alt.EncodingSortField(field='count', op='sum', order='descending')),
                y=alt.Y('count', axis=alt.Axis(labelFontWeight='bold')),
                ).properties(
                title='Distribution of Crime Description based on Female Victims',
                width=600,
                height=400
                ).configure(background='rgba(0,0,0,0)').configure_axis(grid=False)
                st.altair_chart(bar_chart)
                
            with col2:
                top_5 = crime_desc_M.head(5).reset_index()
                st.metric("Tindakan kriminal Tertingi", value=top_5['Crm Cd Desc'][0])
                st.metric("Jumlah Kasus", value=top_5['count'][0])

with tab5:
    _, col2, _ = st.columns([0.5, 2, 0.5])
    with col2:
        st.write('Alfarabi Muzli')
        '''
        ¡Hola! Saya **Alfarabi Muzli**. Terima kasih telah mengunjungi halaman project ini. Halaman ini guna untuk memenuhi capstone project
        DQLab TETRIS Program Batch 4. Saat ini saya masih sangat awam terhadap Data Analisis, jadi kritik dan saran akan sangat membantu untuk meningkatkan
        kemampuan saya. Dibawah ini merupakan kontak penulis. Terima Kasih banyak 🙏.
        '''
        '''
        * :Email: : alfarabi.muzli2909@gmail.com
        * :Github: : https://github.com/tkayha29
        '''
