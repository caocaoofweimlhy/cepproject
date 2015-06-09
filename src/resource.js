var res = {
    HelloWorld_png : "res/HelloWorld.png",
    CloseNormal_png : "res/CloseNormal.png",
    CloseSelected_png : "res/CloseSelected.png",
    jumpright_png: "res/jumpright1.png",
    jumpright_plist: "res/jumpright.plist",
    jumpleft_png: "res/jumpleft1.png",
    jumpleft_plist: "res/jumpleft.plist",
    walk_png:"res/walkright1.png",
    walk_plist:"res/walkright.plist",
    background_png:"res/background.png", 
    token_png: "res/coin1.png",
    token_plist:"res/coin.plist",
    player_png : "res/walkright1.png",
    enemy_png : "res/invader.png",
    ground_png: "res/ground.png",
    platform_png: "res/platform.png",
    wall_png: "res/wall.png"
};

var g_resources = [];
for (var i in res) {
    g_resources.push(res[i]);
}