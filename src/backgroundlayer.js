var BackgroundLayer = cc.Layer.extend({
    ctor:function() {
        this._super();
        var winSize = cc.director.getWinSize();
        var centerPos = cc.p(winSize.width / 2, winSize.height / 2);
        var spriteBG = cc.Sprite.create(res.background_png);
        spriteBG.setPosition(centerPos);
        this.addChild(spriteBG);
    }

});
