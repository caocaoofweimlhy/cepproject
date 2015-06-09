var CoinClass  = cc.Sprite.extend({
    pName:"coin",
    game: null,
    world:null,
    pbody:null,
    shape:null,
    pickupSprite:null,
    pickupAction:null,
    spriteSheet:null,
    exists: true,
    isDynamic:false,
    ctor:function(game,gWorld,posX,posY,id) {
        width = 33;
        height = 36;
        this.world = gWorld;
        this.game = game;

        this.pbody = new cp.Body(1, Infinity);
        this.pbody.setPos(cp.v(posX, posY));

        this.pshape = this.world.addShape(new cp.BoxShape(this.pbody, 20, 20));
        this.pshape.setFriction(10.0);
        this.pshape.setElasticity(0.0);
        this.pshape.setCollisionType("coin");
        this.pshape.name = "coin" + id;

        this.pshape.id = id;
        this.pshape.type = "coin";

        cc.spriteFrameCache.addSpriteFrames(res.token_plist);
        this.spriteSheet = new cc.SpriteBatchNode(res.token_png);
        this.addChild(this.spriteSheet);
        var tokenFrames = [];
        for (var i = 1; i < 8; i++) {
          var str = "coin" + i + ".png";
          var frame = cc.spriteFrameCache.getSpriteFrame(str);
          tokenFrames.push(frame);
        }

        //3.create a animation with the spriteframe array along with a period time
        var animation = new cc.Animation(tokenFrames, 1);
        //4.wrap the animate action with a repeat forever action
        this.tokenAction = new cc.RepeatForever(new cc.Animate(animation));
        this.tokenSprite = new cc.Sprite.create(spriteImage);
        this.game.addChild(this.tokenSprite,0);
        this.tokenSprite.setPosition(posX,posY);
        var spriteImage = res.tokens_png;

        this.tokenSprite.runAction(this.tokenAction);
        this.spriteSheet.addChild(this.tokenSprite);
    },

    remove: function() {
        if(!this.exists) {
            return null;
        } 
        this.world.removeShape(this.pshape);
        this.game.removeChild(this.tokenSprite);
        this.game.addScore();
        this.exists = false;
    }
});