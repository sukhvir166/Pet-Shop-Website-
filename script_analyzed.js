
const IMG={/* images */};
const $=s=>document.querySelector(s),E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const L=(k,d)=>{try{const v=JSON.parse(localStorage.getItem(k));return v==null?d:v}catch(e){return d}},W=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}};
const peso=n=>'₱'+n.toLocaleString('en-PH');
const a=(e,x,y)=>'data:image/svg+xml,'+encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${x}"/><stop offset="1" stop-color="${y}"/></linearGradient></defs><rect width="300" height="300" fill="url(#g)"/><circle cx="150" cy="150" r="105" fill="#fff" fill-opacity=".4" stroke="#fff" stroke-width="6"/><text x="150" y="195" font-size="125" text-anchor="middle">${e}</text></svg>`);
const I=(...k)=>k.map(x=>IMG[x]);
const CATS={food:'Food',toys:'Toys',clothes:'Clothes',beds:'Beds',grooming:'Grooming',essentials:'Essentials',accessories:'Accessories',tracker:'Trackers'};
const P=[
[1,'food','Beef & Veggie Dry Dog Food 1kg',320,[a('🍖','#ffd08a','#f8a62a')]],
[2,'food','Ocean Tuna Cat Pouches, 12 pack',180,[a('🐟','#bfe3ff','#6aa9f5')]],
[3,'food','Chicken Puppy Training Treats',95,[a('🦴','#ffe1b0','#fc7b5f')]],
[4,'food','Salmon Kitten Kibble 1kg',289,[a('🐱','#ffc1d6','#ff7aa8')]],
[5,'food','Dental Chew Sticks, 10 pcs',130,[a('🥕','#d6f5c0','#7cc96a')]],
[6,'food','Gravy Wet Food Cans, 6 pack',410,[a('🥫','#e4d6ff','#9b7bea')]],
[7,'toys','Dog Teething Toy, Puppy Rubber Thorn Bone',70,I(703,708)],
[8,'toys','Pet Chew Toy TPR Ring, Cats and Dogs',75,I(705,706,707)],
[9,'toys','Chew Bone Toy, Pick Your Shape and Size',45,I(709,710,708)],
[10,'toys','Squeaky Plush Duck',99,[a('🦆','#fff3a8','#ffc83d')]],
[11,'toys','Cat Feather Wand Teaser',55,[a('🪶','#ffd6e8','#c18bff')]],
[12,'toys','Cotton Rope Tug Ball',65,[a('🪢','#c9f0ff','#5fc6e8')]],
[13,'clothes','Dog Sunscreen Striped Shirt, for Cats and Small Dogs',250,I(715,716,717,718)],
[14,'clothes','Waffle Bear Dog Vest, Breathable (Shih Tzu, Cats)',85,I(713)],
[15,'beds','Removable, Washable Dog and Cat House Bed (Winter)',518,I(723,725,726,727)],
[16,'grooming','Pawfect Pals Pet Hair Clipper Set with Guide Combs',299,I(749)],
[17,'grooming','AKIIKA 4-in-1 Pet Shampoo 1L, Odor Control, Soft and Shiny Fur',239,I('shampoo2')],
[18,'clothes','Cozy Fleece Hoodie for Pets',220,[a('🧥','#ffd1a6','#fc7b5f')]],
[19,'essentials','Stainless Steel Non-Slip Feeding Bowl',149,[a('🥣','#d8e0ff','#7f8cf0')]],
[20,'essentials','Tofu Cat Litter 6L, Low Dust',260,[a('🧺','#fff0c4','#f2b84b')]],
[21,'accessories','Reflective Collar and Leash Set',165,[a('🦮','#ffd3dc','#ff6f91')]],
[22,'accessories','Breathable Pet Carrier Bag',690,[a('🎒','#d2f3e6','#3fb994')]],
[23,'tracker','Smart GPS Pet Tracker, Waterproof',799,[a('📍','#cfe7ff','#2a6fe0')]],
[24,'tracker','Bluetooth Collar Tag Finder',449,[a('📡','#e8d9ff','#8a5cf0')]],
[25,'beds','Cooling Gel Pet Mat',230,[a('🧊','#cfeeff','#6bb7f0')]],
[26,'beds','Cat Scratcher Lounge',180,[a('🐈','#ffe6c2','#e0a050')]],
[27,'grooming','AKIIKA 4-in-1 Herbal Pet Soap 200g',89,I('soap')],
[28,'grooming','Slicker Brush, Gentle Pins',140,[a('🪮','#ffd9e6','#f27fae')]],
[29,'grooming','Pet Nail Clipper with Guard',120,[a('✂️','#e4e0ff','#8f86e8')]],
[30,'grooming','Ear and Eye Cleaning Drops',160,[a('💧','#d2f2ff','#4fb7e8')]]];
const G=[['food','Food','Fresh bowls for wagging tails',['food']],['toys','Toys','Chew, squeak, tug and play',['toys']],['products','Clothes and beds','Wear it, nap in it',['clothes','beds']],['bath','Bath and grooming','Fresh, soft and shiny fur',['grooming']],['more','Essentials, accessories and trackers','Everyday gear and smart finds',['essentials','accessories','tracker']]];
const PAL=[{n:'Pawdacity',ind:'#1a0a7a',or:'#f8a62a',co:'#fc7b5f',pk:'#ff4f8b',bg:'#fff8ee'},{n:'Ocean',ind:'#0b2a5b',or:'#27b4e0',co:'#4f8cff',pk:'#0aa5a0',bg:'#f1f9ff'},{n:'Forest',ind:'#12361f',or:'#8cc63f',co:'#e8a33d',pk:'#d9544d',bg:'#f6fbef'},{n:'Berry',ind:'#4a0f3d',or:'#ff8fb1',co:'#c94fa0',pk:'#e0245e',bg:'#fff3f8'}];
const D={brand:'Pawdacity',h:'Clean pets, happy hearts!',sub:'Food, toys, cozy beds, clothes and grooming for your cats and dogs, delivered across the Philippines. Every price in pesos.',...PAL[0],fd:'Fredoka',fb:'Nunito',theme:'auto',rad:26,sh:'pop',wall:'none',logo:'',hero:'',wimg:'',ov:{}};
let T={...D,...L('pc_set',{})};
const FONTS=['Fredoka','Baloo 2','Poppins','Quicksand','DM Sans','Nunito','Playfair Display','Lora'];
const WP={none:'',dots:'radial-gradient(#f8a62a66 2px,transparent 2.5px) 0 0/28px 28px',sunset:'linear-gradient(160deg,#ffe9c4,#ffc1a6 55%,#ffb3d1)',mint:'linear-gradient(160deg,#e2fbef,#c7ecff)',lilac:'linear-gradient(160deg,#efe6ff,#ffd9ec)',night:'linear-gradient(160deg,#1b1250,#3b1d7a)'};
const LOGO0=document.querySelector('.lgo').src,HERO0=$('#hi').src,P0=P.map(p=>[...p]);
const save=()=>{if(!W('pc_set',T))toast('Storage full. Use a smaller picture.')};
function ovr(){P.forEach((p,k)=>{const o=T.ov[p[0]]||{};p[2]=o.n||P0[k][2];p[3]=o.p||P0[k][3];p[4]=o.i?[o.i,...P0[k][4].slice(1)]:P0[k][4]})}
function rd(file,w,cb){const r=new FileReader();r.onload=()=>{const i=new Image();i.onload=()=>{const k=Math.min(1,w/Math.max(i.width,i.height)),c=document.createElement('canvas');c.width=i.width*k;c.height=i.height*k;c.getContext('2d').drawImage(i,0,0,c.width,c.height);cb(c.toDataURL('image/jpeg',.82))};i.src=r.result};r.readAsDataURL(file)}
function apply(){const r=document.documentElement,s=r.style,dk=T.theme=='dark'||(T.theme=='auto'&&matchMedia('(prefers-color-scheme:dark)').matches);
T.theme=='auto'?r.removeAttribute('data-theme'):r.dataset.theme=T.theme;
['ind','or','co','pk'].forEach(k=>s.setProperty('--'+k,T[k]));
s.setProperty('--fd',`'${T.fd}',system-ui,sans-serif`);s.setProperty('--fb',`'${T.fb}',system-ui,sans-serif`);s.setProperty('--rad',T.rad+'px');
const h={pop:['6px 6px 0 var(--ind)','6px 12px 0 var(--or)'],soft:['0 10px 28px #1a0a5e33','0 18px 40px #1a0a5e55'],flat:['none','0 0 0 3px var(--or)']}[T.sh];s.setProperty('--shd',h[0]);s.setProperty('--shh',h[1]);
if(dk){s.removeProperty('--bg');s.removeProperty('--ink')}else{s.setProperty('--bg',T.bg);s.setProperty('--ink',T.ind)}
const b=document.body.style;b.background=T.wall=='image'&&T.wimg?`url(${T.wimg}) center/cover`:WP[T.wall]||'';b.backgroundAttachment='fixed';
document.querySelectorAll('.bnm').forEach(e=>e.textContent=T.brand);document.title=T.brand+' – Pet Shop Philippines';
$('#hh').textContent=T.h;$('#hs').textContent=T.sub;document.querySelectorAll('.lgo').forEach(i=>i.src=T.logo||LOGO0);$('#hi').src=T.hero||HERO0}
function tiles(){$('#tl').innerHTML=[['#food','Food',a('🍖','#ffd08a','#f8a62a')],['#toys','Toys',IMG[705]],['#products','Clothes and beds',IMG[713]],['#bath','Bath and grooming',IMG.soap],['#more','Essentials and trackers',a('📍','#cfe7ff','#2a6fe0')]].map(([h,n,s])=>`<a class="tile" href="${h}"><img src="${s}" alt=""><span>${n}</span></a>`).join('')}
function qv(id){const p=P.find(p=>p[0]==id);$('#pb').innerHTML=`<h2 style="font-size:1.3rem">${E(p[2])}</h2><img id="qm" src="${p[4][0]}" alt="" style="width:100%;max-height:50vh;object-fit:contain;background:#fff;border-radius:16px;border:2px solid var(--ind)"><div class="row" style="margin:8px 0;justify-content:flex-start">${p[4].length>1?p[4].map(s=>`<img data-qi src="${s}" alt="" width="54" height="54" style="object-fit:contain;background:#fff;border:2px solid var(--ind);border-radius:10px;cursor:pointer">`).join(''):''}</div><div class="row"><span class="pr">${peso(p[3])}</span><button class="add" data-add="${id}">Add to cart</button></div>`;$('#pd').showModal()}
function ownData(){const us=Object.entries(L('pc_users',{}));return `<details open><summary>Bookings (${bk.length})</summary>${bk.map(b=>`<div class="bk"><b>${E(b.s)}</b><br>${E(b.n||'')} · ${E(b.p)}<br>${E(b.d)}, ${E(b.t)}</div>`).join('')||'<p class="mt">No bookings.</p>'}${bk.length?'<button class="ib" data-cb>Clear all bookings</button>':''}</details><details open><summary>Registered users (${us.length})</summary>${us.map(([e,u])=>`<div class="bk"><b>${E(u.name)}</b> <small>(${E(u.role||'user')})</small><br>${E(e)}${rp[e]?`<br>New password: <b>${E(rp[e])}</b>`:''}<div class="ub"><select data-role="${E(e)}" aria-label="Role"><option ${u.role!='admin'?'selected':''}>user</option><option ${u.role=='admin'?'selected':''}>admin</option></select><button class="rm" data-rp="${E(e)}">Reset password</button><button class="rm" data-du="${E(e)}">Delete</button></div></div>`).join('')||'<p class="mt">No users yet.</p>'}${us.length?'<button class="ib" data-cu>Clear all users</button>':''}</details>${hist()}`}
function devHTML(){return `<button class="devb" data-dev>&gt; About the developer</button><dialog id="dvd" class="dvd"><button class="x" data-close aria-label="Close" style="position:relative;z-index:2;color:#00ff66">×</button><canvas id="mx"></canvas><div class="dv"><h3 class="dn">SUNNY RAJPUT</h3><ul><li>🔭 I’m currently working on <b>Engineering</b></li><li>🌱 I’m currently learning <b>Developer, Enthusiast, AI, ML, DSA, Web frontend and backend, Game design and development, Cyber security, etc.</b></li><li>👨‍💻 All of my projects are available at <a href="https://github.com/sukhvir166" target="_blank" rel="noopener">github.com/sukhvir166</a></li><li>💬 Ask me about <b>Errors, Testing, Reverse Engineering</b></li><li>📫 How to reach me: <a href="mailto:sssrajput166@gmail.com" target="_blank" rel="noopener">sssrajput166@gmail.com</a></li><li>⚡ Fun fact: <b>I am a funny programmer and developer</b></li></ul></div></dialog>`}
let mxT,rp={};function matrix(){clearInterval(mxT)}
function ownRef(){const e=$('#od');if(e)e.innerHTML=ownData()}
const fm=iso=>new Date(iso).toLocaleString('en-PH',{dateStyle:'medium',timeStyle:'short'});
function hist(){const os=L('pc_orders',[]),rev=os.reduce((n,o)=>n+o.t,0);return `<details open><summary>Purchase history (${os.length})</summary><p class="mt">Revenue: ${peso(rev)}</p>${os.map(o=>`<div class="bk"><b>${E(o.name)}</b> <small>${E(o.email)}</small><br><small>${fm(o.at)} · ${E(o.m)} · ${E(o.no)}</small>${o.it.map(i=>`<br>${i.q} × ${E(i.n)} — ${peso(i.p*i.q)}`).join('')}<br><b>Total ${peso(o.t)}</b> <button class="rm" data-do="${E(o.no)}">Delete</button></div>`).join('')||'<p class="mt">No purchases yet.</p>'}${os.length?'<div class="ub"><button class="ib" data-xl>Download Excel (.xlsx)</button><button class="ib" data-ch>Clear history</button></div>':''}</details>`}
async function xl(){const os=L('pc_orders',[]),us=L('pc_users',{});if(!os.length){toast('No purchases to export');return}
const dl=window.claude&&await claude.use('downloads').catch(()=>null);if(!dl){toast('Download is not available in this view');return}
const A=[['Order no','Date','Time','Customer','Email','Product','Qty','Unit price (PHP)','Line total (PHP)','Payment','Order total (PHP)']],pr={},ur={};
os.forEach(o=>{const d=new Date(o.at);o.it.forEach(i=>{A.push([o.no,d.toLocaleDateString('en-CA'),d.toLocaleTimeString('en-GB'),o.name,o.email,i.n,i.q,i.p,i.p*i.q,o.m,o.t]);const k=pr[i.n]||(pr[i.n]=[i.n,0,0]);k[1]+=i.q;k[2]+=i.p*i.q});const u=ur[o.email]||(ur[o.email]=[o.name,o.email,(us[o.email]||{}).role||'user',0,0]);u[3]++;u[4]+=o.t});
const B=[['Name','Email','Role','Orders','Total spent (PHP)'],...Object.values(ur)],C=[['Product','Units sold','Revenue (PHP)'],...Object.values(pr)];
let data,fn='pawdacity-history.xlsx';if(window.XLSX){const wb=XLSX.utils.book_new();[['Purchases',A],['Users',B],['Products',C]].forEach(([n,r])=>XLSX.utils.book_append_sheet(wb,XLSX.utils.aoa_to_sheet(r),n));data=XLSX.write(wb,{bookType:'xlsx',type:'array'})}else{fn='pawdacity-history.csv';data=A.map(r=>r.map(c=>{c=String(c);if(/^[=+\-@]/.test(c))c="'"+c;return '"'+c.replace(/"/g,'""')+'"'}).join(',')).join('\n')}
try{await dl.save({filename:fn,data});toast('Export ready')}catch(e){toast(e&&e.code=='declined'?'Download cancelled':'Download not available here')}}
function sure(t){if(t.dataset.arm){delete t.dataset.arm;return true}t.dataset.arm=1;t.dataset.lb=t.textContent;t.textContent='Tap again to confirm';setTimeout(()=>{if(t.dataset.arm){delete t.dataset.arm;t.textContent=t.dataset.lb}},3000);return false}
function openDev(){const d=$('#dvd');d.showModal();const c=$('#mx'),x=c.getContext('2d'),f=16;c.width=d.clientWidth;c.height=d.scrollHeight;c.style.height=d.scrollHeight+'px';x.fillStyle='#000';x.fillRect(0,0,c.width,c.height);clearInterval(mxT);if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;const y=Array.from({length:Math.ceil(c.width/f)},()=>Math.random()*-40);mxT=setInterval(()=>{if(!d.open)return clearInterval(mxT);x.fillStyle='rgba(0,0,0,.09)';x.fillRect(0,0,c.width,c.height);x.font='bold '+f+'px monospace';y.forEach((v,i)=>{x.fillStyle=Math.random()<.08?'#eaffee':'#00ff66';x.fillText(Math.random()<.5?'0':'1',i*f,v*f);y[i]=v*f>c.height&&Math.random()>.96?0:v+1})},45)}
function ownOpen(){const c=(l,k)=>`<label>${l}<input type="color" data-k="${k}" value="${T[k]}"></label>`,t=(l,k)=>`<label>${l}<input data-k="${k}" value="${E(T[k])}"></label>`,s=(l,k,o)=>`<label>${l}<select data-k="${k}">${o.map(x=>`<option ${x==T[k]?'selected':''}>${x}</option>`).join('')}</select></label>`,u=(l,k)=>`<label>${l}<input type="file" accept="image/*" data-img="${k}"></label>`,g=(n,h)=>`<details open><summary>${n}</summary>${h}</details>`;
$('#own').innerHTML=`<button class="x" data-own aria-label="Close">×</button><h2>Owner panel</h2><p class="mt">Changes apply live and save in this browser. Press Ctrl+K to close.</p>`+
g('Brand and text',t('Shop name','brand')+t('Hero headline','h')+t('Hero text','sub')+u('Logo','logo')+u('Hero picture','hero'))+
g('Colors',`<div class="pal">${PAL.map((p,i)=>`<button data-pal="${i}" style="background:linear-gradient(90deg,${p.ind} 50%,${p.or} 50%)" title="${p.n}" aria-label="${p.n} palette"></button>`).join('')}</div>`+c('Primary (text, borders)','ind')+c('Accent one','or')+c('Accent two','co')+c('Highlight (prices)','pk')+c('Page background','bg'))+
g('Typography',s('Headings font','fd',FONTS)+s('Body font','fb',FONTS))+
g('Theme and appearance',s('Theme','theme',['auto','light','dark'])+s('Card shadow','sh',['pop','soft','flat'])+`<label>Corner roundness<input type="range" data-k="rad" min="6" max="40" value="${T.rad}"></label>`)+
g('Background and wallpaper',s('Wallpaper','wall',[...Object.keys(WP),'image'])+u('Wallpaper picture','wimg'))+
g('Products',`<label>Product<select id="ps">${P.map(p=>`<option value="${p[0]}">${E(p[2]).slice(0,42)}</option>`).join('')}</select></label><label>Name<input id="pn" value="${E(P[0][2])}"></label><label>Price (₱)<input id="pp" type="number" min="1" value="${P[0][3]}"></label><label>New main photo<input id="pi" type="file" accept="image/*"></label><button class="cta" data-sp style="font-size:1rem;padding:8px 18px;margin-top:10px">Save product</button>`)+
`<div id="od">${ownData()}</div><p><button class="ib" data-rs>Reset everything</button></p>${devHTML()}`;$('#own').hidden=false;matrix()}

let f={c:'',q:'',s:'',m:1000},idx={},cart=L('pc_cart',[]),user=L('pc_user',null),bk=L('pc_bk',[]),wl=L('pc_wl',[]),mode='in';
function card(p){const[id,c,n,pr,im]=p,i=idx[id]||0,m=im.length>1;
return `<article class="card"><div class="ph" data-id="${id}"><img src="${im[i]}" alt="${E(n)}" loading="lazy"><span class="tag">${CATS[c]}</span><button class="wl ${wl.includes(id)?'on':''}" data-w="${id}" aria-label="Save to wishlist">♥</button>${m?`<button class="ar l" data-d="-1" aria-label="Previous image">‹</button><button class="ar r" data-d="1" aria-label="Next image">›</button><div class="dots">${im.map((_,j)=>`<i class="${j==i?'on':''}"></i>`).join('')}</div>`:''}</div><div class="bd"><h3>${E(n)}</h3><div class="row"><span class="pr">${peso(pr)}</span><button class="add" data-add="${id}">Add to cart</button></div></div></article>`}
function render(){let h='';G.forEach(([id,t,s,cs])=>{let l=P.filter(p=>cs.includes(p[1])&&(!f.c||(f.c=='__w'?wl.includes(p[0]):p[1]==f.c))&&p[3]<=f.m&&p[2].toLowerCase().includes(f.q));if(f.s)l.sort((x,y)=>f.s=='a'?x[3]-y[3]:y[3]-x[3]);if(l.length)h+=`<section id="${id}"><div class="sh"><h2>${t}</h2><p>${s}</p></div><div class="grid">${l.map(card).join('')}</div></section>`});$('#sec').innerHTML=h||'<p class="empty">No products match. Clear the search or raise the max price.</p>'}
function chips(){$('#chips').innerHTML=[['','All'],['__w','♥ Saved'],...Object.entries(CATS)].map(([k,v])=>`<button class="chip ${f.c==k?'on':''}" data-c="${k}">${v}</button>`).join('')}
function toast(t){const e=$('#toast');e.textContent=t;e.classList.add('s');clearTimeout(toast.t);toast.t=setTimeout(()=>e.classList.remove('s'),2200)}
let cp=L('pc_cp','');const CP={PAW10:['10% off',s=>Math.round(s*.1)],WELCOME50:['₹50 off',s=>Math.min(50,s)],FREESHIP:['Free delivery',()=>0]};
const tot=()=>{const s=cart.reduce((n,x)=>n+x.q*P.find(p=>p[0]==x.id)[3],0),c=CP[cp],ds=c?c[1](s):0,d=!s||s>=999||cp=='FREESHIP'?0:50;return{s,ds,d,t:s-ds+d}};
function drawCart(){W('pc_cart',cart);$('#cn').textContent=cart.reduce((n,x)=>n+x.q,0);$('#cn').classList.remove('bump');void $('#cn').offsetWidth;$('#cn').classList.add('bump');
$('#items').innerHTML=cart.length?cart.map(x=>{const p=P.find(p=>p[0]==x.id);return `<div class="ci"><img src="${p[4][0]}" alt=""><div><b>${E(p[2])}</b><br><small>${peso(p[3])} each</small><div class="q"><button data-q="${x.id}" data-d="-1" aria-label="Less">−</button> ${x.q} <button data-q="${x.id}" data-d="1" aria-label="More">+</button></div></div><div style="text-align:right"><b>${peso(p[3]*x.q)}</b><br><button class="rm" data-rm="${x.id}">Remove</button></div></div>`}).join(''):'<p class="empty">Your cart is empty.<br><a href="#food" data-cx>Browse products</a></p>';
const t=tot();$('#sm').innerHTML=`<div><span>Subtotal</span><span>${peso(t.s)}</span></div>${t.ds?`<div><span>Discount (${cp})</span><span>−${peso(t.ds)}</span></div>`:''}<div><span>Delivery</span><span>${t.d?peso(t.d):'Free'}</span></div><div class="t"><span>Total</span><span>${peso(t.t)}</span></div>`;$('#co').disabled=!cart.length;$('#fp').innerHTML=cart.length?(t.s>=999?'<p class="mt">You get free delivery!</p>':`<p class="mt">Add ${peso(999-t.s)} more for free delivery</p><div class="pg"><i style="width:${Math.min(100,t.s/9.99)}%"></i></div>`)+'<button class="rm" data-cc>Clear cart</button>':''}
function lg(){$('#lg').textContent=user?'Hi, '+user.name.split(' ')[0]+(user.role=='admin'?' (admin)':'')+' (log out)':'Log in'}
function logMode(m){mode=m;$('#lt').textContent=m=='in'?'Log in':'Create account';$('#sw').textContent=m=='in'?'New here? Create an account':'Have an account? Log in';$('#ln').parentNode.querySelector('label[for=ln]').style.display=$('#ln').style.display=m=='in'?'none':'block'}
function pay(){const t=tot();$('#pb').innerHTML=`<h2>Checkout</h2><form id="pf"><label for="pa">Delivery address</label><input id="pa" required placeholder="House no., street, barangay, city"><label for="ph">Mobile number</label><input id="ph" required inputmode="tel" placeholder="09XX XXX XXXX"><div class="pay"><label><input type="radio" name="m" value="GCash" checked> GCash</label><label><input type="radio" name="m" value="Maya"> Maya</label><label><input type="radio" name="m" value="Card"> Credit or debit card</label><label><input type="radio" name="m" value="Cash on delivery"> Cash on delivery</label></div><div id="cf" hidden><input id="cc" placeholder="Card number" inputmode="numeric" maxlength="19"><div class="row"><input id="ce" placeholder="MM/YY" maxlength="5"><input id="cv" placeholder="CVV" maxlength="4" type="password"></div></div><p class="f" style="font-size:1.3rem">Pay ${peso(t.t)}</p><button class="cta" style="width:100%">Place order</button></form>`;
$('#pf').onchange=e=>{$('#cf').hidden=e.currentTarget.m.value!='Card'};
$('#pf').onsubmit=e=>{e.preventDefault();const m=e.target.m.value;if(m=='Card'&&!/^\d{13,19}$/.test($('#cc').value.replace(/\s/g,''))){toast('Enter a valid card number');return}
const no='PAW-'+Date.now().toString().slice(-6),lines=cart.map(x=>x.q+' x '+P.find(p=>p[0]==x.id)[2]).join('%0A');
const os=L('pc_orders',[]);os.unshift({no,name:user.name,email:user.email,at:new Date().toISOString(),m,t:t.t,it:cart.map(x=>{const p=P.find(p=>p[0]==x.id);return{n:p[2],q:x.q,p:p[3]}})});W('pc_orders',os);ownRef();
$('#pb').innerHTML=`<h2>Order placed 🎉</h2><p>Thank you, ${E(user.name)}! Order <b>${no}</b> is confirmed. Paying by <b>${m}</b>: ${peso(t.t)}.</p><p>This is a demo checkout, so no money was charged. Email the order to Pawdacity to finish it.</p><a class="cta" target="_blank" rel="noopener" href="mailto:pawdacity98@gmail.com?subject=Order ${no}&body=${lines}%0ATotal: ${t.t} PHP (${m})%0AAddress: ${encodeURIComponent($('#pa').value)}">Email my order</a>`;cart=[];cp='';W('pc_cp','');drawCart()}}
document.addEventListener('click',e=>{const t=e.target;
if(t.dataset.c!==undefined){f.c=t.dataset.c;chips();render()}
if(t.dataset.add){const x=cart.find(c=>c.id==t.dataset.add);x?x.q++:cart.push({id:+t.dataset.add,q:1});drawCart();toast('Added to cart')}
if(t.dataset.q){const x=cart.find(c=>c.id==t.dataset.q);x.q+=+t.dataset.d;if(x.q<1)cart=cart.filter(c=>c!=x);drawCart()}
if(t.classList.contains('ar')){const id=+t.parentNode.dataset.id,n=P.find(p=>p[0]==id)[4].length;idx[id]=((idx[id]||0)+ +t.dataset.d+n)%n;render()}
if(t.dataset.w){const n=+t.dataset.w;wl=wl.includes(n)?wl.filter(x=>x!=n):[...wl,n];W('pc_wl',wl);render()}
if(t.tagName=='IMG'&&t.closest('.ph'))qv(+t.closest('.ph').dataset.id);
if(t.dataset.qi!==undefined)$('#qm').src=t.src;
if(t.dataset.pal!==undefined){Object.assign(T,PAL[t.dataset.pal]);apply();save();ownOpen()}
if(t.dataset.rs!==undefined&&sure(t)){T=JSON.parse(JSON.stringify(D));save();ovr();apply();ownOpen();render()}
if(t.dataset.own!==undefined)$('#own').hidden=true;
if(t.dataset.dev!==undefined)openDev();
if(t.dataset.du!==undefined&&sure(t)){const us=L('pc_users',{});delete us[t.dataset.du];W('pc_users',us);if(user&&user.email==t.dataset.du){user=null;W('pc_user',null);lg()}ownRef();toast('User deleted')}
if(t.dataset.rp!==undefined){const us=L('pc_users',{}),e1=t.dataset.rp;if(us[e1]){us[e1].pw=rp[e1]='paw'+Math.floor(1000+Math.random()*9000);W('pc_users',us);ownRef();toast('Password reset')}}
if(t.dataset.rm!==undefined){cart=cart.filter(c=>c.id!=t.dataset.rm);drawCart()}
if(t.dataset.cc!==undefined){cart=[];drawCart()}
if(t.dataset.cx!==undefined)$('#drawer').classList.remove('open');
if(t.dataset.do!==undefined&&sure(t)){W('pc_orders',L('pc_orders',[]).filter(o=>o.no!=t.dataset.do));ownRef();toast('Purchase deleted')}
if(t.dataset.ch!==undefined&&sure(t)){W('pc_orders',[]);ownRef();toast('History cleared')}
if(t.dataset.xl!==undefined)xl();
if(t.dataset.cb!==undefined&&sure(t)){bk=[];W('pc_bk',bk);drawBk();ownRef();toast('All bookings cleared')}
if(t.dataset.cu!==undefined&&sure(t)){W('pc_users',{});user=null;W('pc_user',null);lg();ownRef();toast('All users deleted')}
if(t.dataset.sp!==undefined){const id=+$('#ps').value,o=T.ov[id]||(T.ov[id]={}),fl=$('#pi').files[0],fin=()=>{o.n=$('#pn').value;o.p=+$('#pp').value||undefined;save();ovr();render();toast('Product updated')};fl?rd(fl,800,u=>{o.i=u;fin()}):fin()}
if(t.hasAttribute('data-close'))t.closest('dialog').close()});
$('#own').addEventListener('change',e=>{const em=e.target.dataset.role;if(em){const us=L('pc_users',{});if(us[em]){us[em].role=e.target.value;W('pc_users',us);if(user&&user.email==em){user.role=e.target.value;W('pc_user',user);lg()}ownRef();toast('Role updated')}}});
$('#own').addEventListener('input',e=>{const k=e.target.dataset.k;if(k){T[k]=e.target.type=='range'?+e.target.value:e.target.value;apply();save()}});
$('#own').addEventListener('change',e=>{const k=e.target.dataset.img,f1=e.target.files&&e.target.files[0];if(k&&f1)rd(f1,k=='wimg'?1600:900,u=>{T[k]=u;if(k=='wimg')T.wall='image';apply();save();ownOpen()});if(e.target.id=='ps'){const p=P.find(p=>p[0]==e.target.value);$('#pn').value=p[2];$('#pp').value=p[3]}});
document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()=='k'){e.preventDefault();const o=$('#own');o.hidden?ownOpen():o.hidden=true}else if(e.key=='Escape')$('#own').hidden=true});
$('#q').oninput=e=>{f.q=e.target.value.toLowerCase();render()};$('#so').onchange=e=>{f.s=e.target.value;render()};
$('#mx').oninput=e=>{f.m=+e.target.value;e.target.style.setProperty('--v',(f.m-30)/9.7+'%');$('#mv').textContent=f.m;render()};
$('#cb').onclick=()=>$('#drawer').classList.add('open');$('#cx').onclick=()=>$('#drawer').classList.remove('open');
$('#co').onclick=()=>{$('#drawer').classList.remove('open');if(!user){logMode('in');$('#ld').showModal();toast('Log in to check out');return}pay();$('#pd').showModal()};
$('#lg').onclick=()=>{if(user){user=null;W('pc_user',null);lg();toast('Logged out')}else{logMode('in');$('#ld').showModal()}};
$('#sw').onclick=e=>{e.preventDefault();logMode(mode=='in'?'up':'in')};
$('#lf').onsubmit=e=>{e.preventDefault();const em=$('#le').value.trim().toLowerCase(),pw=$('#lp').value,us=L('pc_users',{});
if(mode=='up'){if(us[em]){toast('Email already registered, log in instead');return}us[em]={name:$('#ln').value.trim()||em.split('@')[0],pw,role:'user'};W('pc_users',us)}
else if(!us[em]||us[em].pw!=pw){toast('Wrong email or password');return}
user={name:us[em].name,email:em,role:us[em].role||'user'};W('pc_user',user);lg();ownRef();$('#ld').close();toast('Welcome, '+user.name+'!')};
function drawBk(){$('#bl').innerHTML=bk.length?bk.map(b=>`<div class="bk"><b>${E(b.s)}</b><br>${E(b.p)} · ${E(b.d)}, ${E(b.t)}<br><a target="_blank" rel="noopener" href="mailto:pawdacity98@gmail.com?subject=Appointment%20request&body=${encodeURIComponent((b.n||'')+' - '+b.s+' for '+b.p+' on '+b.d+' at '+b.t)}">Email to confirm</a></div>`).join(''):'<p class="empty">No bookings yet.</p>'}
$('#bd').min=new Date().toISOString().slice(0,10);
$('#bf').onsubmit=e=>{e.preventDefault();const b={s:$('#bs').value,p:$('#bp').value,d:$('#bd').value,t:$('#bt').value,n:$('#bn').value};
if(bk.some(x=>x.d==b.d&&x.t==b.t)){toast('That slot is taken, pick another time');return}
bk.unshift(b);W('pc_bk',bk);drawBk();ownRef();toast('Booked! Tap “Email to confirm” in your bookings');e.target.reset();
};
if(user)$('#le').value=user.email;chips();render();drawCart();drawBk();lg();logMode('in');ovr();apply();tiles();render();
$('#cf').onsubmit=e=>{e.preventDefault();const c=$('#ci2').value.trim().toUpperCase();if(!c){cp='';W('pc_cp','');drawCart();toast('Coupon removed');return}if(!CP[c]){toast('Invalid coupon code');return}cp=c;W('pc_cp',cp);drawCart();toast(CP[c][0]+' applied')};
