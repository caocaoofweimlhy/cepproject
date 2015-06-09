var world;
var gameScene = cc.Scene.extend({
    player: null,
    enemies: [],
    ecount: 0,
    coins: [],
    statics: {},
    removeArr: [],
    backgroundLayer: null,
    statusLayer: null,
    onEnter: function() {
        this._super();
        winSize = cc.director.getWinSize();
        this.backgroundLayer = new BackgroundLayer();
        this.addChild(this.backgroundLayer);
        this.statusLayer = new StatusLayer();
        this.addChild(this.statusLayer);
        world = new cp.Space();
        world.gravity = cp.v(0, -100);
        var debugDraw = cc.PhysicsDebugNode.create(world);
        debugDraw.setVisible(false);
        this.addChild(debugDraw);

        this.createStatic(Infinity, Infinity, 240, 0, 500, 15, 1.0, 0.0, res.ground_png, 0);
        this.createStatic(Infinity, Infinity, 225, 40, 100, 24, 1.0, 0.0, res.platform_png, 1);
        this.createStatic(Infinity, Infinity, 300, 150, 100, 24, 1.0, 0.0, res.platform_png, 2);
        this.createStatic(Infinity, Infinity, 100, 150, 100, 24, 1.0, 0.0, res.platform_png, 3);
        this.createStatic(Infinity, Infinity, 15, 240, 10, 400, 10.0, 0.0, res.wall_png, 4);
        this.createStatic(Infinity, Infinity, 465, 240, 10, 400, 10.0, 0.0, res.wall_png, 5);

        this.player = new PlayerClass(this, world, 50, 15);
        this.coins[0] = new CoinClass(this, world, 440, 50, 0);
        this.coins[1] = new CoinClass(this, world, 420, 200, 1);
        this.coins[2] = new CoinClass(this, world, 300, 250, 2);
        this.coins[3] = new CoinClass(this, world, 100, 200, 3);

        var listener = cc.EventListener.create({
            event: cc.EventListener.TOUCH_ONE_BY_ONE,
            swallowTouches: true,
            onTouchBegan: function(touch, event) {
                var target = event.getCurrentTarget();
                var location = target.convertToNodeSpace(touch.getLocation());
                var s = target.getContentSize();
                var rect = cc.rect(0, 0, s.width, s.height);
                if (cc.rectContainsPoint(rect, location)) {
                    if (touch.getLocationX() >= s.width / 2) {
                        target.playJumpright(touch.getLocationX(),touch.getLocationY());
                    } else {
                        target.playJumpleft(touch.getLocationX(),touch.getLocationY());
                    }
                    return true;
                }
                return false;
            }
        });

        cc.eventManager.addListener(listener, this);

        world.env = this;
        world.setDefaultCollisionHandler(this.beginCollision,this.preCollision,this.postCollision,null);
        this.schedule(this.spawn, 2);
        this.scheduleUpdate();

    },

    update:function(dt) {
        world.step(dt);
        if(this.player.isAlive) {
            this.player.updatePosition();
        }
        for(var i = 0; i < this.enemies.length; i++) {
            if(this.enemies[i].pbody.p.y < 0) {
                this.enemies[i].remove();
                continue;
            }
            this.enemies[i].updatePosition();
        }
        for(var j = 0; j < this.removeArr.length; j++) {
            if(this.removeArr[j].type == "coin") {
                this.coins[this.removeArr[j].id].remove();
            } else if(this.removeArr[j].type == "player") {
                this.statusLayer.gameOver();
                this.player.remove();
            }
            this.removeArr.splice(j, 1);
        }
    },

    spawn: function() {
        this.enemies[this.ecount] = new EnemyClass(this, world, 40 + Math.random() * 400, 750);
        this.ecount++;
    },

    createStatic: function(mass, moment, x, y, width, height, friction, elasticity, spriteImage, id) {
        var staticSprite = new cc.Sprite.create(spriteImage);
        this.addChild(staticSprite, 0);
        staticSprite.setPosition(x, y);

        var staticBody = new cp.Body(mass, moment);
        staticBody.setPos(cp.v(x, y))

        var staticShape;
        staticShape = new cp.BoxShape(staticBody, width, height);
        staticShape = world.addShape(staticShape);
        staticShape.setFriction(friction);
        staticShape.setElasticity(elasticity);
        staticShape.setCollisionType("static");
        staticShape.name = "static" + id;
        this.statics["static" + id] = staticShape;
    },
    playJumpright: function(curX, curY) {
        this.player.startJumpright(curX, curY);
    },
    playJumpleft: function(curX, curY) {
        this.player.startJumpleft(curX, curY);
    },

    activateJump: function() {
        this.player.canJump = true;
    },

    beginCollision: function(arbiter, space) {
        if(arbiter.a.collision_type == "enemy" && arbiter.b.collision_type != "player" ||
            arbiter.a.collision_type != "player" && arbiter.b.collision_type == "enemy") {
            return false;
        }
        return true;
    },

    preCollision: function(arbiter, space) {
        if(arbiter.a.collision_type == "player" && arbiter.b.collision_type == "coin") {
            space.env.removeArr.push(arbiter.b);
            return false;
        } else if(arbiter.a.collision_type == "coin" && arbiter.b.collision_type == "player") {
            space.env.removeArr.push(arbiter.a);
            return false;
        } else if(arbiter.a.collision_type == "player" && arbiter.b.collision_type == "enemy") {
            space.env.removeArr.push(arbiter.a);
            return false;
        } else if(arbiter.a.collision_type == "enemy" && arbiter.b.collision_type == "player") {
            space.env.removeArr.push(arbiter.b);
            return false;
        }
        return true;
    },

    postCollision: function(arbiter, space) {
        if(arbiter.a.collision_type == "player" && arbiter.b.collision_type == "static" ||
            arbiter.a.collision_type == "static" && arbiter.b.collision_type == "player") {
            space.env.activateJump();
        }
    },
    addScore: function() {
        this.statusLayer.addScore(1);
    }
});